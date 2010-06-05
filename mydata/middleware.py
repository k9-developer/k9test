from k9test.mydata.models import HttpReq


class HttpReqSave:
    def process_request(self, request):
        req = HttpReq()
        req.path = request.path
        req.save()

