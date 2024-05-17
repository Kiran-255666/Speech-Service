---
lab:
    title: 'Translate Speech'
    module: 'Module 8 - Translate speech with Azure AI Speech'
---

# Translate Speech

Azure AI Speech includes a speech translation API that you can use to translate spoken language. For example, suppose you want to develop a translator application that people can use when traveling in places where they don't speak the local language. They would be able to say phrases such as "Where is the station?" or "I need to find a pharmacy" in their own language, and have it translate them to the local language.



## Clone the repository for this course



1. Start Visual Studio Code.
2. Open the palette (SHIFT+CTRL+P) and run a **Git: Clone** command to clone the 'https://github.com/Kiran-255666/Speech-Service` repository to a local folder (it doesn't matter which folder).
3. When the repository has been cloned, open the folder in Visual Studio Code.


## Provision an Azure AI Speech resource

If you don't already have on in your subscription, you'll need to provision a **Azure AI Speech service** resource.

1. Open the Azure portal at `https://portal.azure.com`, and sign in using the Microsoft account associated with your Azure subscription.
1. Enter **Azure AI** in the search field at the top of the portal. Then select **Azure AI services** in the suggestions dropdown that appears.
1. Select **Create** under **Speech service** in the results page.
1. Create a resource with the following settings:
    - **Subscription**: *Your Azure subscription*
    - **Resource group**: *Choose or create a resource group (if you are using a restricted subscription, you may not have permission to create a new resource group - use the one provided)*
    - **Region**: *Choose any available region*
    - **Name**: *Enter a unique name*
    - **Pricing tier**: Standard S0
1. Select **Review + Create,** then select **Create**.
1. Wait for deployment to complete, and then view the deployment details.
1. When the resource has been deployed, go to it and view its **Keys and Endpoint** page. You will need one of the keys and the location in which the service is provisioned from this page in the next procedure.

## Prepare to use the Azure AI Speech Translation service

In this exercise, you'll execute the client application that uses the Azure AI Speech SDK to recognize, translate, and synthesize speech.


1. In Visual Studio Code, in the **Explorer** pane, Open **Speech-Services** folder.
2. Right-click the **translator** folder and open an integrated terminal. Then install the Speech SDK package and other packages by running the foloowing commands.

    ```

    pip install azure-cognitiveservices-speech==1.30.0
    
    ```
    
    ```
    pip install playsound==1.3.0
    ```

3. Expand the  **translator** folder and click on translator.py to open the file. Then Replace the cog_key and cog_region with your Azure Speech service key and region in which speech service is deployed.Then Save the file using CTRL+S.
4. In the terminal type **python translator.py** to run the translator.py file.
5. When prompted, enter a valid language code (*fr*, *es*, or *hi*). The program should transcribe your audio input and respond with a spoken translation. Repeat this process, trying each language supported by the application. When you're finished, press **ENTER** to end the program.


## More information

For more information about using the Azure AI Speech translation API, see the [Speech translation documentation](/azure/ai-services/speech-service/speech-translation).
