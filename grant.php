<?php
$oauthAuthorizationURL =<Paste Value from OAuth Authorization URL Here in Double Quotes>;
?>

<!DOCTYPE html>
<html>
  <head>
    <title>Get a Webex OAuth authorization code</title>
    <meta charset='utf-8'>
  </head>
  <body>
        <h1>Get a Webex OAuth authorization code</h1>
        </div>
        <div class='spacer-small'></div>
        <div class='center'>

<?php
echo "<a href=\"" . $oauthAuthorizationURL . "\">";
?>

            <div class='button' style='width:512px;'>GRANT</div>
          </a>
        </div>
      </div>
    </section>
  </body>
</html>