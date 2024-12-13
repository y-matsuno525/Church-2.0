// 座標とズームレベルを指定 例：東京
const map = L.map('map').setView([36.903587544438906, 140.13628169999998], 10);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    // 右下にクレジットを表示
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// マーカー
//新フッタライト大輪キリスト教会
var marker = L.marker([36.903587544438906, 140.13628169999998]).addTo(map);
marker.bindPopup("<b>New Hutterite Daiwa Christian Church</b><br>A faith community in the tradition of the Anabaptist Hutterites")
.openPopup();