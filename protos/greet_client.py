import greet_pb2_grpc
import greet_pb2
import time
import grpc

def get_client_stream_requests():
    while True:
        name = input("plice enter a name (or nothing to stop chatting): ")

        if name == " ":
            break
        hello_request = greet_pb2.HelloRequest(greeting = "Hello",name = name)
        yield hello_request
        time.sleep(1)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1.SayHello -Unary")
        print("2.ParrotSayHello -Server Side Streaming")
        print("3.ChattyClientSayHello -Client Side Streaming")
        print("4.InteractingSayHello -Both Streaming")

        rpc_call = input("Which rpc would you like to make: ")

        if rpc_call == "1":
            hello_request = greet_pb2.HelloRequest(greeting = "Bonjour", name="YouTube")
            hello_reply = stub.SayHello(hello_request)
            print("SayHello Response Recived:")
            print(hello_reply)

        elif rpc_call == "2":
            hello_request = greet_pb2.HelloRequest(greeting="Bonjour", name="youtube")
            hello_replies = stub.ParrotSaysHello(hello_request)

            for hello_reply in hello_replies:
                print("ParrotSaysHello Response Recived:")
                print(hello_reply)

        elif rpc_call == "3":
            delayed_reply = stub.ChattyClientSaysHello(get_client_stream_requests())

            print("ChattyClientSaysHello Response Recived:")
            print(delayed_reply)
                
        elif rpc_call == "4":
            print("Not Implemented")

if __name__ == "__main__":
    run()