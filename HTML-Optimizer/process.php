<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ข้อมูลคำสั่งซื้อ</title>
    <h1>ขอบคุณสำหรับการสั่งซื้อนะง้าบบบบ</h1>
</head>
<body>
    <?php
        if ($_SERVER["REQUEST_METHOD"] == "GET") {
 
            $fullname = htmlspecialchars($_GET['fullname'] ?? '');
            $province = htmlspecialchars($_GET['province'] ?? '');
            $address = htmlspecialchars($_GET['address'] ?? '');
            $iphone = $_GET['iphone'] ?? [];
            $iphoneList = !empty($iphone) ? implode(", ", array_map('htmlspecialchars', $iphone)) : 'ไม่ได้เลือก';
            $color = $_GET['color'] ?? [];
            $colorList = !empty($color) ? implode(", ", array_map('htmlspecialchars', $color)) : 'ไม่ได้เลือก';
            $storage = htmlspecialchars($_GET['storage'] ?? 'ไม่ได้เลือก');
            $number = htmlspecialchars($_GET['number'] ?? 'ไม่ได้เลือก');
            $payment = htmlspecialchars($_GET['payment'] ?? 'ไม่ได้เลือก');
 
            echo "<h1>ข้อมูลที่ส่งมา</h1>";
            echo "<p><b>ชื่อ-นามสกุล:</b> $fullname</p>";
            echo "<p><b>จังหวัด:</b> $province</p>";
            echo "<p><b>ที่อยู่:</b><br>" . nl2br($address) . "</p>";
            echo "<p><b>สินค้า:</b> $iphoneList</p>";
            echo "<p><b>วิธีการจัดส่ง:</b> $colorList</p>";
            echo "<p><b>จำนวน:</b> $number เครื่อง</p>";
            echo "<p><b>วิธีชำระเงิน:</b> $payment</p>";
        } else {
            echo "<p>ไม่พบข้อมูล หรือส่งข้อมูลไม่ถูกต้อง</p>";
        }
    ?>
</body>
</html>
 
        