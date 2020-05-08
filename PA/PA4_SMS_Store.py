import time

class SMS_Store:
    def __init__(self):
        self.add = []

    def view_all(self):
        for i in self.add:
            print(i)

    def message_count(self):
        message = print("Count of messages are {}".format(len(self.add)))
        return message

    def add_new_arrival(self, number, time, message):
        self.add.append(("Has been viewed : False", "From : {0} , Time : {1} , Message : {2}".format(number, time, message)))

    def get_unread_indexes(self):
        unread_Message = []
        for (i, j) in enumerate(self.add):
            if j[0] == "Has been viewed : False":
                unread_Message.append(i)
        return unread_Message


    def get_message(self, i):
        try:
            msg = self.add[i]
            msg = ("Has been viewed : True",) + msg[1:]
            self.add[i] = (msg)
            return print(self.add[i])

        except IndexError:
            return None

    def delete(self, i):
        try:
            del self.add[i]
            print("Messsage Deleted")

        except IndexError:
            print("Index Range Overed!!")


    def clear(self):
        self.add = []
        print("No Messages!!")



if __name__ == '__main__':
    time_stamp = time.time()
    time = time.ctime(time_stamp)

    my_inbox = SMS_Store()

    my_inbox.add_new_arrival("010-2805-3454", time, "Hi Hello Bonjour")
    my_inbox.add_new_arrival("010-xxxx-xxxx", time, "Hufs Ice")
    my_inbox.add_new_arrival("010-yyyy-yyyy", time, "Internet Application")
    my_inbox.add_new_arrival("010-zzzz-zzzz", time, "201602560 Jaesung Lee")

    print("=" * 23 + " All Messages " + "=" * 23)
    my_inbox.view_all()
    my_inbox.message_count()
    print()

    print("=" * 20 + " Delete 2nd message " + "=" * 20)
    my_inbox.delete(1)
    print()

    print("=" * 21 + " Remain Messsages " + "=" * 21)
    my_inbox.view_all()
    print()

    print("=" * 19 + " Unread Messages count " + "=" * 18)
    print(my_inbox.get_unread_indexes())
    print()

    print("=" * 23 + " Get Messages " + "=" * 23)
    my_inbox.get_message(1)
    print()

    print("=" * 21 + " Remain Messsages " + "=" * 21)
    my_inbox.view_all()
    print()

    print("=" * 21 + " Clean Messages " + "=" * 21)
    my_inbox.clear()









