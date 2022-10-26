<?php

$bearer_token = "Enter Your Token Here in Double Quotes";
$userToReset = $_POST["listbox"];
$curlGetUserList = curl_init();
$curlResetPin = curl_init();

curl_setopt_array($curlGetUserList, array(
  CURLOPT_URL => 'https://webexapis.com/v1/people',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'GET',
  CURLOPT_HTTPHEADER => array(
    'Authorization: Bearer ' . $bearer_token,
  ),
));

curl_setopt_array($curlResetPin, array(
  CURLOPT_URL => 'https://webexapis.com/v1/people/' . $userToReset . '/features/voicemail/actions/resetPin/invoke',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'Authorization: Bearer ' . $bearer_token,
  ),
));

$userListJSON = curl_exec($curlGetUserList);
curl_close($curlGetUserList);

$userListPHPObject = (json_decode($userListJSON, true));
$users = array_keys($userListPHPObject["items"]);
?>

<html>
  <body>
  <form action="/pinreset.php" method="POST" id="form1">

<?php
        if(isset($_POST['resetButton'])) {            
            
            curl_exec($curlResetPin);            
            curl_close($curlResetPin);
            echo "Voicemail PIN Has Been Reset to Organization Default.";
        }
?>

    <p>Choose a User for Voicemail PIN reset<br>
    <select name="listbox" size="5" style="width: 200px;">

<?php
        foreach($users as $user){
          echo "<option value=\"" . $userListPHPObject["items"][$user]["id"] . "\">" . $userListPHPObject["items"][$user]["emails"][0] . "</option>";
        }
?>

   </select>
      </p>
      <input type="submit" name="resetButton" value="Reset PIN">
    </form>
  </body>
</html>