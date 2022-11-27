from duplipy import DuplicateDetector

dd = DuplicateDetector()
l = ["test", "test2", "test"]
dd.fit(l)

print(dd.data)
