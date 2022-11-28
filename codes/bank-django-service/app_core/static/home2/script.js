import GetUserAccount from "/static/home2/GetUserAccount.js"
import GetBalance from "/static/home2/GetBalance.js"

// 載入使用者帳號
async function load_account() {    
    user_account.innerHTML = await GetUserAccount();
    balance_text.innerHTML = '$'+ await GetBalance();
}

// 主函數
function main() {
    load_account();
}

// 當頁面完全載入後啟動主函數
window.onload = function () {
    main()
}