---
title: "How to Use the Tableau App"
article_id: 39250660729747
url: "https://support.optisigns.com/hc/en-us/articles/39250660729747-How-to-Use-the-Tableau-App"
updated_at: "2026-01-06T22:36:49Z"
---

### In this article, we’ll show you how to set up and use the Tableau app to display Dashboards on digital signs.

* What You’ll Need
* Step 1: Set Up OptiSigns as a Connected App in Tableau
* Step 2: Set Up Tableau Integration in OptiSigns
* Step 3: Creating a Tableau Asset
* Additional Notes

With the Tableau app, it’s possible to securely display Tableau dashboards on your large TVs and screens. This can dramatically increase communication and information across office spaces.

To do this, you’ll need to follow three steps:

1. ## What You’ll Need

   * Pro Plus subscription or greater
   * set up and paired with OptiSigns
   * Managing User Roles for more information.

   ---

   ## Step 1: Set Up OptiSigns as a Connected App in Tableau Cloud

   To view Private reports in OptiSigns, it needs to be set up as a **Connected App** in Tableau Cloud. If you’re only interested in displaying Public reports, this step can be skipped - however, we ***highly recommend*** it, as setting up this integration will allow you to use it for any future reports you want to display from this account. If you are only interested in displaying Public reports, though, feel free to [skip to step 3](#Step3).

   To begin, find your **Settings** tab within Tableau. Once there, click **Connected Apps** → **New Connected App**.

   ![new connected app tableau](https://support.optisigns.com/hc/article_attachments/39250613919635)

   Select **Direct Trust**.

   ![direct trust dropdown tableau](https://support.optisigns.com/hc/article_attachments/39250613922451)

   You’ll open the Create Connected App window. Here, you can give your connected app a name (we recommend “OptiSigns” so you know it’s for us), restrict its access, and provide allowed domains. For the purposes of this example, we’ll apply it to “All projects” and “All domains.”

   ![create connected app window tableau](https://support.optisigns.com/hc/article_attachments/39250613923987)

   Once created, it will appear in a list of Connected Apps. Select the app.

   On this screen, you'll want to **Enable** the OptiSigns app by hitting the **Three Dots**. Then, you'll want to hit **Generate New Secret**:

   ![Screenshot 2025-03-22 at 5.27.26 PM.jpg](https://support.optisigns.com/hc/article_attachments/39672709375507)

   The blurred out values are your **Secret ID, Secret Value, and Client ID**. These values will be critical to setting up your integration with OptiSigns, so keep this tab open.

   With this information and the app Enabled in Tableau, we can configure the integration in OptiSigns.

   ---

   ## Step 2: Set Up Tableau Integration in OptiSigns

   Before starting this step, you should have:

   1. Under the Tableau section of the Integrations page, select **Add Connection**.

      ![](https://support.optisigns.com/hc/article_attachments/39597853563283)

      The **Add** window will pop up:

      ![add integrations window optisigns](https://support.optisigns.com/hc/article_attachments/39250613933203)  
      You’ll need to fill in 5 values:

      * the last step.
      * ## Step 3: Create a Tableau Asset and Assign it to a Screen

        Now that we’ve got the Tableau integration set up, it’s time to create a Tableau asset. This asset determines how your report will show up on your screens.

        |  |
        | --- |
        | **NOTE** |
        | See [**Note 2**](#Note2) if your workbook contains Broad Views. |

        First, find the report you’d like to display. Hit **Share:**

        ![](https://support.optisigns.com/hc/article_attachments/39364492002579)

        On the Share View window, hit **Copy Link**:

        ![share view copy link tableau](https://support.optisigns.com/hc/article_attachments/39250613936275)

        Now go back to the OptiSigns portal and hit **Files/Assets** → **Apps:**

        ![optisigns files/assets tab app](https://support.optisigns.com/hc/article_attachments/39250613937555)

        Now find the **Tableau** app.

        ![tableau app optisigns](https://support.optisigns.com/hc/article_attachments/39250660711955)

        Clicking the app will open this window:

        ![](https://support.optisigns.com/hc/article_attachments/39597827693203)

        + Steps 1 and [2](#Step2), we recommend ticking this box. If you skipped those steps and only want to use Public reports, no need to check the box.

        |  |
        | --- |
        | **NOTE** |
        | Tableau Cloud only allows 600 Update Interval requests per user/hour. See [**Note 3**](#Note3) for more information and solutions on how to handle this. |

        Now it's time to authenticate your Shared Report URL with an appropriate Connected App Integration you set up earlier:

        ![](https://support.optisigns.com/hc/article_attachments/39597827694099)

        + you set up in Step 2 in this box.

        Once you input the **Tableau Shared Report URL** and have selected your Integration, hit **Save** and your report should appear as a Preview:

        ![](https://support.optisigns.com/hc/article_attachments/39597827695763)

        Once you have tailored it to your liking, you can **Close** it. This will create a Tableau asset that can be added to a Playlist or directly assigned to a screen:

        ![](https://support.optisigns.com/hc/article_attachments/39597853567251)

        In order to display different tabs of a report, select the tab you'd like to view on Tableau site, then hit **Share**, same way as before:

        ![tableau report share](https://support.optisigns.com/hc/article_attachments/39250660703635)

        You'll then create a new Asset with that Share link as the **Site URL**:

        ![](https://support.optisigns.com/hc/article_attachments/39597827698067)

        To display all the tabs in a report on a screen, these Assets can be placed in a [Playlist](https://support.optisigns.com/hc/en-us/articles/28295104605843-How-to-Create-Use-Playlists) to show the complete report.

        ## Additional Notes

        #### Note 1

        Content display may vary based on device type and screen resolution.

        #### Note 2

        **If your workbook contains broad views:**

        + Fit Width, **Fit Height**, or **Entire View**:  
          ![](https://support.optisigns.com/hc/article_attachments/39597827704979)

   #### Note 3:

   [Tableau currently limits](https://help.tableau.com/current/online/en-us/to_site_capacity.htm) its maximum number of refresh requests to 600 per hour/user. This means you'll want to be careful on how you set the "Update Interval," especially if you have numerous devices wanting to display Tableau reports.

   We have several recommendations on how to handle this with multiple devices:

   1. **Data Freshness Policy**which limits the number of refreshes of a workbook using a live connection. This is a setting within Tableau that controls your refresh rate.

      To change this, go to the workbook you want to edit. Hit the **Info button** **→ Edit Freshness Policy...** then click **Ensure data is fresh every:** and set it to your desired freshness.

      ![](https://support.optisigns.com/hc/article_attachments/47980799604755)

      There are a few critical points to note here.

      * That’s all!

        OptiSigns is the leader in [digital signage software](https://www.optisigns.com/). If you have any additional questions, concerns or any feedback about OptiSigns, feel free to reach out to our support team at [support@optisigns.com](mailto:support@optisigns.com).

---

Source: https://support.optisigns.com/hc/en-us/articles/39250660729747-How-to-Use-the-Tableau-App
