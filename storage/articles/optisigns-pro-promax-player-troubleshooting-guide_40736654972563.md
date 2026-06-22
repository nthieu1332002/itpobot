---
title: "OptiSigns Pro/ProMax Player Troubleshooting Guide"
article_id: 40736654972563
url: "https://support.optisigns.com/hc/en-us/articles/40736654972563-OptiSigns-Pro-ProMax-Player-Troubleshooting-Guide"
updated_at: "2026-01-13T21:20:16Z"
---

### In this article, we troubleshoot the most common issues our customers face when using an OptiSigns Pro or ProMax Player.

* Best Practices
* The Troubleshooting Option
* Hardware Troubleshooting
  + Network Troubleshooting
  + Power, HDMI & TV Connection Troubleshooting
  + Blank Screen Troubleshooting
  + Fixing the OnHold Warning
  + App Freezes, Video Assets not Playing full video or Asset Not Loaded Fully
  + How to Factory Reset the OptiSigns Pro/ProMax Player
* Security Settings Troubleshooting
  + Using the Device Log
  + Static IP
  + Internal Websites and Root Certificates
* Pro/ProMax Player RMA Process

If you’ve got an OptiSigns Pro or ProMax Player and you’re having issues, you’ve come to the right place. For first time setup, see our [**Set Up the OptiSigns Pro Player**](https://support.optisigns.com/hc/en-us/articles/32272215514131-Optisigns-Pro-Digital-Signage-Player) or [**Set Up the OptiSigns ProMax Player**](https://support.optisigns.com/hc/en-us/articles/38680194603155-OptiSigns-ProMax-Player) articles. For more on the Pro or ProMax player features, see our [**Advanced Features**](https://support.optisigns.com/hc/en-us/articles/35577511423635-OptiSigns-Pro-Player-Advanced-Features) article.

---

## Best Practices

* **Mobile Admin App**. This will allow you to use numerous features remotely, including the Remote Keyboard app and remote monitoring.
* ## The Troubleshooting Option

  Your first stop when running into a problem with the OptiSigns Pro or ProMax player should be the **Troubleshooting** page. This is an option on the Side Menu:

  ![troubleshooting page menu location](https://support.optisigns.com/hc/article_attachments/40736654908563)

  Choosing this option will open the Troubleshooting screen:

  ![troubleshooting screen](https://support.optisigns.com/hc/article_attachments/40736654909587)

  + **Whitelist Article** for the required URLs and ports.
* ## Hardware Troubleshooting

  Here we will cover the most common hardware troubleshooting issues our support team encounters with our OptiSigns Pro and ProMax players. Following these steps will resolve 90%+ of issues.

  ### Network Troubleshooting

  This is, by far, the most common issue people encounter. Devices experiencing network issues typically appear “Offline” in the OptiSigns portal, even when they are powered on and have content assigned to them.

  ![optisigns screen offline](https://support.optisigns.com/hc/article_attachments/40736654910739)

  The first stop should be the [**Troubleshooting Page**](#TroubleshootingOption). The upper left box details network status. If all the text is green, this means there are no network issues. Any red text will require further troubleshooting.

  To identify and resolve network issues:

  + **Whitelist Article** for the required URLs and ports.
  + **Factory Reset** the device, then perform initial setup again.
  + **contact our support team**. After a bit of troubleshooting, you may be asked to submit an [**RMA request**](#RMAProcess)**.**

  ### Power Cable, HDMI & TV Connection Troubleshooting

  + ### Blank Screen Troubleshooting

    If your device and screen are on, but only displays a black screen:

    - **Whitelisted OptiSigns IP addresses and ports**.
    - **Factory Reset**.

      ### Fixing the OnHold Warning

      ![OnHold warning](https://support.optisigns.com/hc/article_attachments/40736684864403)

      This warning displays when the device is in the [**OnHold Folder**](https://support.optisigns.com/hc/en-us/articles/1500003244381-About-the-OnHold-Devices-Folder). This happens when you’ve ordered more devices than you had licenses for. Any devices above your license limit will automatically be placed in the OnHold folder and will need to be removed, even when the license limit has been raised.

      ### App Freezes, Video Assets not Playing full video or Asset Not Loaded Fully

      To handle any of these issues, hit the **Refresh & Relaunch** option of the OptiSigns Player, then reboot. You may need to Factory Reset if the problem persists.

      ### How to Factory Reset an OptiSigns Pro or ProMax Player

      Sometimes, it might be necessary to perform a factory reset on your OptiSigns Pro Player.

      To do this, attach a keyboard to the Player. Then, **Reboot** it. As it restarts, rapidly tap the **↑ arrow** (the **End** key may also work). It will boot into this screen:

      ![optisigns pro player boot screen](https://support.optisigns.com/hc/article_attachments/40736654916499)

      Here, you have several additional options. Hit **Factory Reset**. You’ll receive this prompt:

      ![factory reset password screen](https://support.optisigns.com/hc/article_attachments/40736654917395)

      You’ll need to enter your **admin password.**

      Once entered, you’ll see a screen like this:

      ![factory reset in progress](https://support.optisigns.com/hc/article_attachments/40736684873363)

      Afterwards, your factory defaults will be restored.

      ---

      ## Security Settings and Advanced Feature Troubleshooting

      The Pro and ProMax Players offer advanced security settings and features that are indispensable for an enterprise environment. Below are the most common and helpful suggestions we have when trying to enable some of these more advanced settings.

      See our [**Pro/Pro Max Player Advanced Features**](https://support.optisigns.com/hc/en-us/articles/35577511423635-OptiSigns-Pro-Player-Advanced-Features) article for information on setting these up.

      ### Using the Device Log

      There are two ways to use the **Device Log** feature:

      1. 2. **Remote Command** from the OptiSigns portal. This will provide a download link that you can use to obtain the log:

         ![execute remote command device log](https://support.optisigns.com/hc/article_attachments/40736684875283)

         This can be extremely helpful for troubleshooting any issues that might have occurred when the device was not being closely monitored.

         ### Static IP

         When setting up a Static IP, make sure you’ve selected the appropriate static IP setting, depending on whether you’re using a WLAN or Ethernet connection.

         ![static IP wlanip vs ethip](https://support.optisigns.com/hc/article_attachments/40736684876691)

         Next, ensure you’ve input the correct information in the IP Address, Default Gateway, Subnet Mask, and DNS Server fields.

         ![static ip options](https://support.optisigns.com/hc/article_attachments/40736654945427)

         See our [**Advanced Settings for the Pro/ProMax Player**](https://support.optisigns.com/hc/en-us/articles/35577511423635-OptiSigns-Pro-Player-Advanced-Features) article for more information.

         ### Internal Website and Certificates

         For installation on a Gen 3 Pro or ProMax Player, your certificate must have a **.crt** extension. However, it is important that this certificate is signed and contains your public key. These are usually generated as **.pem** files. You’ll need to rename your certificate (.pem) file and change its extension to **.crt** for your internal website to properly display.

         ![certificate file option](https://support.optisigns.com/hc/article_attachments/40736684879635)

         See our article on [**how to install a root certificate and set up your internal website display**](https://support.optisigns.com/hc/en-us/articles/35184720136595-How-to-Install-a-Root-Certificate-and-Display-an-Internal-Website-on-Screens) for more information.

         ---

         ## Pro/ProMax Player RMA Process

         Please try to go through the above common troubleshooting steps before submitting an RMA request.

         Devices will be tested in the RMA process. If they work normally, the customer will be charged a restocking fee.

         Our RMA process is as follows:

         * **this RMA form** (with proof of purchase in the last 12 months).
         * support@optisigns.com.

---

Source: https://support.optisigns.com/hc/en-us/articles/40736654972563-OptiSigns-Pro-ProMax-Player-Troubleshooting-Guide
