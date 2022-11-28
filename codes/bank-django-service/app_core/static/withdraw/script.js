import GetUserAccount from "/static/home2/GetUserAccount.js"
import GetBalance from "/static/home2/GetBalance.js"

// 載入使用者帳號
async function load_account() {    
    user_account.innerHTML = await GetUserAccount();
}

// 載入餘額
async function load_balance() {
    balance_text.innerHTML = '$'+ await GetBalance();
    window.setInterval(async ()=>{
        balance_text.innerHTML = '$'+ await GetBalance();
    }, 1000);
}

// 主函數
function main() {

}

// 當頁面完全載入後啟動主函數
window.onload = function () {
    main()
}