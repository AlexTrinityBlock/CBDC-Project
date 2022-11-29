import GetBalance from "/static/pay/GetBalance.js"

// 載入餘額
async function load_balance() {
    window.setInterval(async () => {
        balance_text.innerHTML = '$' + await GetBalance();
    }, 1000);
}

// 主函數
function main() {
    load_balance();
}

// 當頁面完全載入後啟動主函數
window.onload = function () {
    main()
}