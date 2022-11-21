class ResolveRequest:
    def __init__(self):
        pass
    
    @staticmethod
    def ResolveToken(request):
        # 無論GET或者POST都接收，之後依照需求修改
        if request.method == 'GET':
            data = request.GET
        elif request.method == 'POST':
            data = request.POST

        # 檢查Token 是否正確，同時相容token存在於cookie或者request中。
        if "token" in data:
            token = data["token"]
        elif "token" in request.COOKIES:
            token = request.COOKIES["token"]

        return token

    @staticmethod
    def ResolvePost(request):
        if request.method == 'POST':
            return request.POST
        else:
            raise Exception("方法錯誤")