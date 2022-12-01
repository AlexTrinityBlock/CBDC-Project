class AdministratorLoginMiddleware:
    """
    管理員登入驗證中間層
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.admin_login_require_page = [
            # 'administrator/home/',
        ]
    
    def check_path_in_list(self,path:str):
        for path_in_list in self.admin_login_require_page:
            if path == ('/' + path_in_list):
                return True
        return False

    def __call__(self, request):
        require_login = self.check_path_in_list(request.path)
        response = self.get_response(request)
        
        return response
