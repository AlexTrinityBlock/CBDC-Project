from django.shortcuts import redirect
from app_core.services.ResolveRequest import ResolveRequest

class AdministratorLoginMiddleware:
    """
    管理員登入驗證中間層
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # 登錄要登入的頁面
        self.admin_login_require_page = [
            'administrator/home',
            'administrator/issue/voucher'
        ]
    
    def check_path_in_list(self,path:str):
        for path_in_list in self.admin_login_require_page:
            if path == ('/' + path_in_list):
                return True
        return False

    def __call__(self, request):
        # 嘗試取得登入使用者角色
        try:
            role = ResolveRequest.ResolveRole(request)
        except:
            role = None

        require_login = self.check_path_in_list(request.path)
        if require_login and (role != 'administrator'):
            return redirect("/administrator/login")
        response = self.get_response(request)
        
        return response
