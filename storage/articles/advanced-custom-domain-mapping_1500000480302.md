---
title: "Advanced: Custom Domain mapping"
article_id: 1500000480302
url: "https://support.optisigns.com/hc/en-us/articles/1500000480302-Advanced-Custom-Domain-mapping"
updated_at: "2026-05-29T17:34:19Z"
---

With OptiSigns Pro Plus and Enterprise plan, you can enhance your branding by mapping your custom domain for OptiSigns Management Portal.

For example: you can map your sub-domain: **login.abcmedia.com** so that your users can log in and use the portal from **login.abcmedia.com** and use the app like the screenshot below.

![mceclip0.png](https://support.optisigns.com/hc/article_attachments/1500000517302)

#### **Let's jump in and get started!**

**1) Activate your OptiSigns sub-domain (in this example: abcmedia.optisigns.net):**

Go to the Branding page of your Account Management Settings:

<https://app.optisigns.com/app/s/branding-settings>

Type in your desired sub-domain for optisigns.net. In this case, we type in "abcmedia".  
Don't worry about optisigns.net, you will map your domain in the next step.

![mceclip2.png](https://support.optisigns.com/hc/article_attachments/360099399934)

**2) Map CNAME alias for your domain/sub-domain:**

In your Domain DNS management, map your desired domain/sub-domain to your OptiSigns sub-domain using CNAME Alias.  
In this example, we map: login.abcmedia.com -> abcmedia.optisigns.net

Refer to your domain host documentation for more specific details.

Here are the generic steps:

1. **CNAME Record**


   | Record type | Label/Host field | Time To Live (TTL) | Destination/Target field |
   | --- | --- | --- | --- |
   | CNAME | login | 3600 or leave the default | abcmedia.optisigns.net |
2. GoDaddy
3. Namecheap
4. Bluehost
5. 1&1 IONOS
6. HostGator
7. DreamHost
8. Cloudflare

**3) Activate SSL for your sub-domain**

Once you have done step 2, return to the Branding page:

<https://app.optisigns.com/app/s/branding-settings>

Enter the domain/sub-domain you have configured in Step 2 in Your domain section.

In this example, we use: login.abcmedia.com

Then click Activate.

This will trigger the process on OptiSigns side to activate SSL for your sub-domain. This will ensure that your user can use HTTPS: i.e. <https://login.abcmedia.com> to use the app.

This process can take up to 24-48 hours to complete. You will be notified via email once it's done.

![mceclip3.png](https://support.optisigns.com/hc/article_attachments/360101613533)

#### **That's all!**

Once you get the notification that your SSL is activated, you can start using your own domain/sub-domain (i.e. <https://login.abcmedia.com>).

---

Source: https://support.optisigns.com/hc/en-us/articles/1500000480302-Advanced-Custom-Domain-mapping
