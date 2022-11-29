import GetBalance from "/static/deposit_upload/GetBalance.js"
import RedeemCurrency from "/static/deposit_upload/RedeemCurrency.js"
import GetPaymentID from "/static/deposit_upload/GetPaymentID.js"

// 載入餘額
async function load_balance() {
    window.setInterval(async () => {
        balance_text.innerHTML = '$' + await GetBalance();
    }, 1000);
}

// 處理上傳檔案
function file_handler() {
    currency_file.addEventListener('change',async (event) => {
        // 讀取檔案
        let file = await event.target.files[0];
        let filexText = await file.text();
        let currency = JSON.parse(filexText);
        // 寫入變數
        let Info = currency.Info
        let message = currency.message
        let t = currency.t
        let s = currency.s
        let R = currency.R
        // 取得支付ID
        let payment_id = await GetPaymentID()
        // 開啟等待圓球
        upload_spinner.style.display = "block";
        // 關閉上傳按鈕
        currency_file.style.display = "none";
        // 傳送給銀行
        let result= await RedeemCurrency(payment_id,message,Info,R,s,t)
        // 關閉等待圓球
        upload_spinner.style.display = "none";
        // 開啟上傳按鈕
        currency_file.style.display = "block";
        // 清除上傳內容
        currency_file.value = null
    });
}

// 主函數
function main() {
    load_balance();
    file_handler();
}

// 當頁面完全載入後啟動主函數
window.onload = function () {
    main()
}
