import random, time

random.seed(time.time())

MAX_SIMUL_TIME = 10
MAX_PRINTING_TIME = 5
JOB_ARRIVAL_PROB = 0.4

queue = []
current_time = 0
job_id = 1
current_job = None
remaining_time = 0

while current_time < MAX_SIMUL_TIME:
    print(f"\n----- time {current_time} -----")

    # 새로운 job 도착
    if random.random() < JOB_ARRIVAL_PROB:
        duration = int(random.random() * MAX_PRINTING_TIME) + 1
        queue.append({"id": job_id, "duration": duration})
        print(f"새 jop <{job_id}>이 들어 왔습니다. 프린트 시간은 = {duration} 입니다.")
        job_id += 1

    # 현재 작업이 없거나 끝났을 때 → 바로 다음 job 실행 (대기 메시지 출력 안 함)
    if remaining_time <= 0:
        if current_job:
            print(f"jop <{current_job['id']}>의 프린트가 완료되었습니다.")
        if queue:
            current_job = queue.pop(0)
            remaining_time = current_job["duration"]
            print(f"프린트를 시작합니다 - jop <{current_job['id']}> ...")
        else:
            current_job = None  # 대기 메시지는 생략
    else:
        print(f"아직 jop <{current_job['id']}>을 프린트하고 있습니다 ...")
        remaining_time -= 1

    # 큐 상태 출력
    print("현재 프린터 큐 :", "[ " + " ".join(str(j["id"]) for j in queue) + " ]")

    current_time += 1

