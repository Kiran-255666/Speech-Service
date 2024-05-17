---
lab:
    title: 'Translate Speech'
    module: 'Module 8 - Translate speech with Azure AI Speech'
---

# Translate Speech

Azure AI Speech includes a speech translation API that you can use to translate spoken language. For example, suppose you want to develop a translator application that people can use when traveling in places where they don't speak the local language. They would be able to say phrases such as "Where is the station?" or "I need to find a pharmacy" in their own language, and have it translate them to the local language.

> [!NOTE]
> This exercise requires that you are using a computer with speakers/headphones. For the best experience, a microphone is also required. Some hosted virtual environments may be able to capture audio from your local microphone, but if this doesn't work (or you don't have a microphone at all), you can use a provided audio file for speech input. Follow the instructions carefully, as you'll need to choose different options depending on whether you are using a microphone or the audio file.

## Clone the repository for this course



1. Start Visual Studio Code.
2. Open the palette (SHIFT+CTRL+P) and run a **Git: Clone** command to clone the '(https://github.com/Kiran-255666/Speech-Service.git)` repository to a local folder (it doesn't matter which folder).
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


1. In Visual Studio Code, in the **Explorer** pane, Open **08-speech-translation** folder and expand the **C-Sharp** or **Python** folder depending on your language preference.
1. Right-click the **translator** folder and open an integrated terminal. Then install the Speech SDK package by running the appropriate command for your language preference:

    ```

    **Python**

    ```python
    pip install playsound==1.3.0
    ```


    **Python**

    ```python
    python translator.py
    ```

1. When prompted, enter a valid language code (*fr*, *es*, or *hi*), and then speak clearly into the microphone and say a phrase you might use when traveling abroad. The program should transcribe your spoken input and respond with a spoken translation. Repeat this process, trying each language supported by the application. When you're finished, press **ENTER** to end the program.

> [!NOTE]
> *In this example, you've used a **SpeechTranslationConfig** to translate speech to text, and then used a **SpeechConfig** to synthesize the translation as speech. You can in fact use the **SpeechTranslationConfig** to synthesize the translation directly, but this only works when translating to a single language, and results in an audio stream that is typically saved as a file rather than sent directly to a speaker.*

## More information

For more information about using the Azure AI Speech translation API, see the [Speech translation documentation](/azure/ai-services/speech-service/speech-translation).
