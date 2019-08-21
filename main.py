from router import Router


def hello_world():
    print("hello world")


if __name__ == "__main__":
    router = Router()
    router.add_route('GET', '',  hello_world, hello_world, hello_world)
