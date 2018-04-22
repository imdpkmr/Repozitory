# Repozitory
Django based application for a storing documents, files etc.
The  app name is ‘Docstore’. It is kept as symbolic to document storehouse.
 
The home link shows us the page as shown in above image. It is a default tabular display of all the artifacts (we will be calling all our research material as artifacts from here on). The primitive display has only Artifact Id, Name, Category and Type in the display. User can type any search criteria in the ‘search; option available, and also restrict the total number of records displayed at any time.
All these Artifact Name entries are clickable:
 
As shown above, point to any artifact and clicking it will lead to a detailed display of information about the artifact.
 
As we can see in the above screenshot, detailed view shows the name of the artifact, its category and type along with its creation and last updated time stamps. There is yet another field displayed below ‘last updated’, called as ‘Remark’, which holds in some descriptive meta about the artifact, so that it is easy for user to read and spot specific artifacts among similar ones.
There are three functionalities in form of buttons on this page. 
1)	Download – User can download a file if exists/attached with the artifact. This can very well be a textual document, an image or a video.
 
2)	Update ¬¬– Clicking on the Update button takes user to a page where he/she can edit some information about the artifact.
 
3)	Delete – Clicking on this will delete the artifact from repozitory and redirect user to home page.
 

After details view, we will show you how to add a new artifact, on top right corner we can see a menu option ‘Add Artifact’. Click it, enter details and save. You will be redirected to home page on successful save.
 
 
Along with these, there is yet another functionality of signing up users. As a future development, I have left this to be able to create sessions and add a ‘last updated by’ field as well in the artifacts model. There is also ‘Admin Login’ which lets logging into the Django application Admin page.
 
 
Admin can add / remove users and artifacts from database.
 
 

On entering unique username, email and then a valid password, django will allow to add it as a new user.

models.py
Consists of only one model ‘Artifact’ which has the following fields:
1)	Docname  - name for the artifact
2)	Category – Technical, Finance or Marketing
3)	Type – Images, documents or Videos
4)	Created At – timestamp for creation
5)	Updated At – timestamp for updates on artifact
6)	Remark – short description for the artifact
7)	Artifact file – a file associated with the artifact
Along with these, every artifact has a unique numeric ‘id’ or ‘pk’ which gets default associated in django models.
