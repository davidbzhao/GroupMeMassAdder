# GroupMe Mass Adder

A little script to add a lot of people to a GroupMe group

## Usage

### 1. Getting the code
* Clone or download this repository

### 2. Getting a GroupMe token
* Go to [dev.groupme.com](https://dev.groupme.com/) and login using your GroupMe credentials
* In the upper-right hand, you'll see a "Access Token" button. Click on that and copy your access token
* Create `auth.yml` and copy `test.yml` into it
* Paste the token into auth.yml file, replacing "TOKEN"

 ### 3. Defining members to add
* Create a .csv file and copy `test.csv` into it
* Following that format, paste in all the members you want to add

### 4. Executing the script
* With python3, run `python add.py`.
* Input the group you want to add members to (case-sensitive)
* Input the path (relative or absolute) to the .csv file with all the members you want to add
* Verify the response is 202