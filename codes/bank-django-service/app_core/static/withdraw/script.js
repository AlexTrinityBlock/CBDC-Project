import GetBalance from "/static/withdraw/GetBalance.js"
import Withdraw from "/static/withdraw/Withdraw.js"
import Cookies from "/static/cookie-js/js.cookie.min.mjs"
import GetToken from "/static/withdraw/GetToken.js"

// var url = "http://192.168.230.252:8086/withdraw"
var url = "/api/withdraw/test"

// 載入餘額
async function load_balance() {
    window.setInterval(async () => {
        balance_text.innerHTML = '$' + await GetBalance();
    }, 1000);
}

// UUID
async function uuidv4() {
    return ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, c =>
        (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    );
}

//建立 QR code
async function qr_code(text) {
    let qrcode = new QRCode(document.getElementById("qr_code"), {
        colorDark: "#0066cc",
        correctLevel : QRCode.CorrectLevel.L,
    });
    qrcode.makeCode(text);
}

// 提領貨幣
async function handle_withdraw() {
    withdraw_btn.addEventListener('click', async function (e) {
        // 取得貨幣
        let withdraw_number = withdraw_input.value
        let token = await GetToken();//取得使用者識別
        let currency = await Withdraw(token, withdraw_number, url);//取得貨幣
        balance_text.innerHTML = '$' + await GetBalance();//更新貨幣數量
        // 生成檔案
        var blob = new Blob([currency],
            { type: "text/plain;charset=utf-8" });
        saveAs(blob, "貨幣." + await uuidv4() + ".txt");
        //  彈跳視窗

        Swal.fire({
            icon: 'success',
            title: '提款成功 !',
            confirmButtonText: '取得QR code',
            allowOutsideClick: false,
        }).then((result) => {
            Swal.fire({
                title: '貨幣 QR code',
                html: '<div id="qr_code"></div>',
                confirmButtonText: '關閉',
                allowOutsideClick: false,
            })
            qr_code(currency)
        })

        withdraw_input.value = 0
    }, false);
}

// 主函數
function main() {
    load_balance();
    handle_withdraw();
}

// 當頁面完全載入後啟動主函數
window.onload = function () {
    main()
}