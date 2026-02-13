'''
def instagram(func):
    def wrapper(*args,**kwargs):
        print("www.insta.com")
        print("Logged in")
        func(*args,**kwargs)
        print("Logged out")
    return wrapper

@instagram
def shubham_insta():
    print("Msg to friend")

@instagram
def nitish_insta():
    print("Watched some reels")


shubham_insta()
nitish_insta()

'''
class Demo:
    a = 10
    b =20
ob1 =Demo()

print(ob1.a)
print(ob1.b)
print(Demo.a)
print(Demo.b)