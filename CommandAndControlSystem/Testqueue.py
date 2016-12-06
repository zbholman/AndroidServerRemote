def worker():
        while True:
                item = q.get()
                do_work(item)
                q.task_done()

def Queue(self):
	for i in range(5):
		t = Thread(target=worker)
		t.daemon = True
		t.start()

	for item in source():
		q.put(item)

	q.join()
