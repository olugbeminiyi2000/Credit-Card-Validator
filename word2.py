Response1
Traceback (most recent call last):
  File "C:\Users\obolo\lemur\response1\response1.py", line 119, in <module>
    main()
  File "C:\Users\obolo\lemur\response1\response1.py", line 85, in main
    manager = TaskManager()
  File "C:\Users\obolo\lemur\response1\response1.py", line 8, in __init__
    self.tasks = self.load_tasks()
  File "C:\Users\obolo\lemur\response1\response1.py", line 13, in load_tasks
    return json.load(file)
  File "C:\Users\obolo\AppData\Local\Programs\Python\Python39\lib\json\__init__.py", line 293, in load
    return loads(fp.read(),
  File "C:\Users\obolo\AppData\Local\Programs\Python\Python39\lib\json\__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "C:\Users\obolo\AppData\Local\Programs\Python\Python39\lib\json\decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "C:\Users\obolo\AppData\Local\Programs\Python\Python39\lib\json\decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)


Response2
Task Manager Menu:
1. Add Task
2. Display Tasks
3. Delete Task
4. Mark Task as Completed
5. Check Overdue Tasks
6. Exit
Enter your choice: 
