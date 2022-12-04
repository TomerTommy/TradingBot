import ibapi.wrapper as wrapper
import ibapi.client as client

testWrapper = wrapper.EWrapper

class TestClient(client):
        def __init__(self, wrapper):
            client.__init__(self, wrapper)

class TestApp(testWrapper, TestClient):
        def __init__(self):
            testWrapper.__init__(self)
            TestClient.__init__(self, wrapper=self)

        