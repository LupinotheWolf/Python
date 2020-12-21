from formatting import format_msg

def send(name):
    msg = format_msg(name)
    return msg

class Animal:
    noise = None
    weight = None

    def make_noise(self):
        print(f"{self.noise}")
    def disp_weight(self):
        print(f"{self.weight}")

    def set_noise(self, new_noise):
        self.noise = new_noise
        return self.noise
    def set_weight(self, new_weight):
        self.weight = new_weight
        return self.weight
