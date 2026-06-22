---
title: "Operational Schedule Troubleshooting"
article_id: 48241081473043
url: "https://support.optisigns.com/hc/en-us/articles/48241081473043-Operational-Schedule-Troubleshooting"
updated_at: "2026-04-20T21:26:17Z"
---

### In this article, we will troubleshoot common issues related to the Operational Schedule feature in OptiSigns.

* Introduction to Operational Scheduling
* Changing Display Settings
* How to Test HDMI-CEC / RS-232 Connections
* OptiStick Improperly Powered
* Operational Schedule Works at Different Times from How It Was Set
* Screen Turns Off, But Not Back On

Operational Scheduling is a feature which allows you to turn off and on your digital signs on a set schedule, further automating your setup. If you’re looking to set up an Operational Schedule of your own, see our guide on [Creating and Using Operational Schedules](https://support.optisigns.com/hc/en-us/articles/28598173096723-How-To-Create-and-Use-Operational-Schedules-HDMI-CEC-RS-232).

However, many factors and settings may need adjustment in order to get this feature running properly. Here, we go through a few of the most common troubleshooting scenarios our teams face.

---

## **Introduction to Operational Scheduling**

Operational Schedule allows you to schedule when your TV powers on/off and to control the volume and brightness through the device level, HDMI-CEC, or RS-232 connections. HDMI-CEC is a popular feature available on most consumer TVs right now, while RS-232 is useful for commercial-grade displays.

|  |
| --- |
| Limitations |
| * | |
| * **OptiSigns OptiStick**, [**Pro Signage Player**](https://shop.optisigns.com/products/optisigns-digital-signage-player), or [**ProMax Player**](https://support.optisigns.com/hc/en-us/articles/38680194603155-OptiSigns-ProMax-Player). The player will need to be plugged in to an HDMI-CEC port to function. RS-232 functionality can be used with any device which supports it.   + **TV Manufacturer CEC Names**. Simply find your device on the list and enable HDMI-CEC, if necessary. This will solve a lot of issues by itself.        ---        Changing Display Settings In order for Operational Scheduling to work, your TV must actually support it. Operational Scheduling makes use of either:      - HDMI-CEC settings to find your display’s make and model for information on how to set this up to receive signal.     - |  |       | --- |       | **NOTE** |       | Your device will try RS-232 first if available, then HDMI-CEC command to turn off TV/Monitor. Your TV/Monitor model and player needs to support this feature for it to work. Players sold by OptiSigns support HDMI-CEC and RS-232. | |

On most displays, HDMI-CEC or RS-232 will need to be enabled before Operational Scheduling will work. How to do this will vary by TV and connection.

|  |  |
| --- | --- |
| **MORE ON RS-232** | |
| An RS-232 cable should have come with your display. We recommend using this if possible, as there are reportedly issues with certain displays (generally LG) when other RS-232 cables are used.  Your RS-232 ports may look different depending on the age of your display: | |
| **OLDER DISPLAYS:** | **NEWER DISPLAYS:** |
|  |  |
| A typical RS-232 cable which comes with most new commercial displays: | |
| [**Buy USB-A to RS-232 cable for older displays**](https://www.amazon.com/Sabrent-Converter-Prolific-Chipset-CB-DB9P/dp/B00IDSM6BW?dib=eyJ2IjoiMSJ9.eDpH7mZ-MxF1rW_bLcNPOgxDhwo8eCgqihSClktQT86m8ERQwz21Q9euBmQ3zNtrIG2huqPq1a_Yupg_0lAfJD7XCkjpxXR7vDb_WG-28D3-SuPxCy1MVPvoKFbVWg92YGOfKork7n_l1CNOzUJ-R9gMzzuw9iQpODbta2oRWS1vbcaQF9XyY0RrYG6443FJHjRAL09KvJaZCY_6khThywKVe_gaB5qpCHxZzBMbRFk.gkxWaA_HDwYQYoAZKJYArVgEQjxmvGUftl17_EdW9Z0&dib_tag=se&keywords=db9%2Bto%2Busb&qid=1768493612&sr=8-3&th=1) | * **Buy USB-A to RS-232 cable for newer displays** * **Buy USB-A to RS232 Female Adapter** |

---

## How to Test HDMI-CEC / RS-232 Connections

Here is how to test your HDMI-CEC or RS-232 connection to make sure it works as it should.

Go to **Edit Screen → Advanced → More**:

Click the **Arrow** in the right hand corner of the popup, next to the **Save** option. This will bring up several options. Hit **Send HDMI CEC** or **Send RS232**:

![](https://support.optisigns.com/hc/article_attachments/48241081464467)

This should either turn on or turn off the TV depending on whether the TV is currently on or off. If it does not, keep troubleshooting.

---

## OptiStick Improperly Powered

It is possible to power the OptiStick via a USB port on your display. However, in addition to [the other problems this causes](https://support.optisigns.com/hc/en-us/articles/40147900639891-OptiStick-Troubleshooting-Guide#Power), powering an OptiStick via USB will cause significant problems with the Operational Schedule feature.

Think about it this way: your OptiStick is tasked with powering down and powering off your display, but it is relying on that display to pull power from. Once the display is off, how is the OptiStick supposed to turn it back on? There is no power reaching it. That’s why it needs its own dedicated power source (i.e. outlet) to use Operational Scheduling properly.

For this reason, if you want to make use of Operational Scheduling with an OptiStick, ***be sure to plug it into a dedicated outlet, not the USB port.***

---

## Operational Schedule Works at Different Times from How It Was Set

This is very common and almost always goes back to the device Time Zone. Your first troubleshooting step for this issue should be to set the time zone.

This can be done either with the device itself, or remotely (if the device is online). To update it remotely, edit the screen, then hit **Advanced**. You should see the below bar, click the **Time Zone** button:

![](https://support.optisigns.com/hc/article_attachments/48241081465107)

This will open up the **Update Time Zone** screen:

![](https://support.optisigns.com/hc/article_attachments/48241081468307)

Here, simply select the appropriate Time Zone for your device. This should match the Operational Schedule you’ve set to it. Now, they should be aligned.

---

## Screen Turns Off, But Not Back On

One of the main reasons for this is that the [OptiStick is improperly powered](#ImproperlyPowered). However, another possible reason (regardless of the device being used) is that Operational Scheduling might not be supported on your individual TV, regardless of settings. This is a limitation of the device.

Assuming the OptiStick is plugged into a wall socket and this issue persists, here is what you can try:

* USB-to-RS232 cable usually fixes these issues. For Pro/ProMax users, this [3.5mm-to-RS232 cable](https://www.amazon.com/Wpeng-Female-3-5mm-Serial-Conversion/dp/B06WLP4LTP?crid=2TJVY9W17FGXA&dib=eyJ2IjoiMSJ9.Y6_VGAouYwBNLtnwPYqjn-7cydyPVjGKK0bAEUGUF8eIUkzSYL1ZP9NZRBcu05_r1XxGY3Z1QvyptSulXNnCQH125i4Jjfgx2Qt0uSAmgg2Wgdm3XwCtixWVVfdMD_n8r0nKRjLWXHtwauI8uI6MUHKhfuv7g4U1CM6IpPvwo4wo5eG0AUrFo4h52R25zD1XtpLffAo54EJDoy2rHtJuiQwlKBtci_9Wl5_6seGMHLk.EMlyYI-DF9Ak6MFx4QxzmJVovu79dk4VaYEdXmMZXs8&dib_tag=se&keywords=rs232+cable+jack&qid=1768421592&sprefix=rs232+cable+jac%2Caps%2C169&sr=8-3) will also work.

If you've tried the above, feel free to [reach out to our support team](https://support.optisigns.com/hc/en-us/articles/35626165056787-How-to-Contact-OptiSigns-Support).

### That’s all!

Still having problems with getting your Operational Schedule to work? Reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com) for additional help.

---

Source: https://support.optisigns.com/hc/en-us/articles/48241081473043-Operational-Schedule-Troubleshooting
