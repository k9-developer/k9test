from k9test.mydata.models import HttpReq
import random

class HttpReqSave:
    def process_request(self, request):
        req = HttpReq()
        req.path = request.path
        req.priority = random.randint(0, 1)
        req.save()
