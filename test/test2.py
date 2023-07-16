a = {}

def func():
    a["x"] = "y"
    import test1
    print(len(a))

if __name__ == "__main__":
    func()