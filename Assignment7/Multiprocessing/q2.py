from multiprocessing import Process, Pipe


def sender(parent_conn):
    parent_conn.send('Hiiiiii')
    parent_conn.close()


def reciever(child_con):
    print("Message received :", child_con.recv())


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()  # returns two conn object
    sender_process = Process(target=sender, args=(parent_conn,))
    reciever_process = Process(target=reciever, args=(child_conn,))
    sender_process.start()
    reciever_process.start()
