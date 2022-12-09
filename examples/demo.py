from duplipy import DuplicateDetector

dd = DuplicateDetector()
# list
data1 = [
    "the cat sat in the hat",
    "the cat sat on the mat",
    "we all scream for ice scream",
    # "we all scream for ice cream",
    # "we all like ice scream",
    # "abcdefg",
    # "abcdefg\nhijklmnop"
]
# dict
data2 = [{abs(hash(element)): element} for element in data1]

# dict with another structure
data3 = {
    "id": [0, 1, 2],
    "text": ["the cat sat in the hat", "the cat sat on the mat", "we all scream for ice scream"],
}


dd.fit(data3)

for k, v in dd.data.items():
    print(k, v)
