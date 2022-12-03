import GetBalance from "/static/redeem_voucher/GetBalance.js"
import RedeemVoucher from "/static/redeem_voucher/RedeemVoucher.js"

// 載入餘額
async function load_balance() {
    balance_text.innerHTML = '$' + await GetBalance();
    window.setInterval(async () => {
        balance_text.innerHTML = '$' + await GetBalance();
    }, 1000);
}

// QR code scanner 
async function qr_scanner() {
    const html5QrCode = new Html5Qrcode("reader");
    const config = { fps: 10, qrbox: { width: 1000, height: 1000 } };
    html5QrCode.start({ facingMode: "environment" }, config, (decodedText, decodedResult) => {
        html5QrCode.stop()
        process_2(decodedText)
    });
}

// 支付步驟1
async function process_1() {
    qr_scanner();
}

// 支付步驟2
async function process_2(decodedText) {
    let redeemResult = await RedeemVoucher(decodedText)
    console.log(redeemResult.code)
    if (redeemResult.code == 1) {
        Swal.fire({
            icon: 'success',
            title: '儲值成功 !',
        })
    }
    init()
}

// 初始化支付
async function init() {
    await new Promise(r => setTimeout(r, 500));
    process_1();
}

// 主函數
function main() {
    load_balance();
    process_1();
}

// 當頁面完全載入後啟動主函數
window.onload = function () {
    main()
}