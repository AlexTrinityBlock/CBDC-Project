import GetBalance from "/static/pay/GetBalance.js"

// 載入餘額
async function load_balance() {
    window.setInterval(async () => {
        balance_text.innerHTML = '$' + await GetBalance();
    }, 1000);
}

// 啟動網路攝影機
async function webCam() {
    const html5QrCode = new Html5Qrcode("reader");

    const config = { fps: 10, qrbox: { width: 250, height: 250 } };

    html5QrCode.start({ facingMode: "environment" }, config, (decodedText, decodedResult) => {
        console.log('Success')
        html5QrCode.stop()
    });
}

// 主函數
function main() {
    load_balance();
    webCam();
}

// 當頁面完全載入後啟動主函數
window.onload = function () {
    main()
}