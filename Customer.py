class Customer:
    def __init__(self, id, fname, lname, address, mobile):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.address = address
        self.mobile = mobile

    def __str__(self):
        return f'id: {self.id}, name: {self.fname} {self.lname}, address: {self.address}, mobile: {self.mobile}'

    def __repr__(self):
        return f'Customer({self.id}, {self.fname}, {self.lname}, {self.address}, {self.mobile})'

    def __eq__(self, other):
        return (
                isinstance(other, Customer) and
                self.lname == other.lname and
                self.address == other.address
        )

    def __hash__(self):
        return hash(self.lname)
