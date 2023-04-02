# financial-lead-analysis
README
Prerequisites
Git installed on your system
Java Runtime Environment (JRE) installed on your system
Python 3 installed on your system
JBoss Enterprise Application Platform (EAP) installer downloaded from https://developers.redhat.com/products/eap/getting-started
Installation

Clone this repository using the following command:

bash
Copy code
git clone  https://github.com/406solutions/financial-lead-analysis.git)


Navigate to the cloned repository and run the install_libraries.sh script to install the required libraries:

bash
Copy code
cd yourproject
./install_libraries.sh


Create a new Python environment by running the env.sh script:

bash
Copy code
source env.sh


Run the main.py script to start the application:

css
Copy code
python main.py


Install JBoss EAP by following the instructions provided in the downloaded installer.

Deploy a container from the JBoss EAP GUI interface.

Running the JBoss EAP Text-based Installer
Open a terminal and navigate to the directory containing the downloaded JBoss EAP Installer JAR.
Run the text-based installer using the following command:
javascript
Copy code
java -jar jboss-eap-7.x.x-installer.jar -console

Follow the prompts to install JBoss EAP. The directory created by the installer is the top-level directory for the server. This is referred to as EAP_HOME.
