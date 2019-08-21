from router import Router


def hello_world():
    print("hello world")


if __name__ == "__main__":
    router = Router()
    router.add_route('GET', '/(?P<word>)',  hello_world, hello_world, hello_world)
    route = router.find_route('/hello')
    pass

