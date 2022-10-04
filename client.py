import AdHocComm as ac

newUDPClient = ac.AdHocComm()

jsonData = {
        "key1" : "Hello",
        "key2" : "World",
        "key3" : 888,
        "key 4" : {"123" : 456, "testing" : 123}
    }

newUDPClient.sendUDP("127.0.0.1", str(jsonData))
newUDPClient.sendUDP("127.0.0.1", str(jsonData))
newUDPClient.sendUDP("127.0.0.1", str(jsonData))
