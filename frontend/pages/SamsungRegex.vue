<template>
  <div>
    <h2 style="text-align: center;">Samsung Regular Expression Automatic Labeler</h2>
    <div class="file-upload-container">
        <div
        class="file-drop"
        v-if="!fileUploaded"
        @dragover.prevent
        @drop="handleFileDrop"
        >
        <p>Drag and drop a .csv file here</p>
        </div>
        <div v-else>
        <p v-if="!downloadUrl">File Successfully Uploaded!</p>
            <div v-if="loading" class="loading-animation">
            <!-- You can replace this with your loading animation HTML/CSS -->
            <div class="loader"></div>
            </div>
        </div>
        <input
        type="file"
        ref="fileInput"
        accept=".txt"
        style="display: none"
        @change="handleFileChange"
        v-if="!fileUploaded"
        />
        <button @click="openFileInput" v-if="!fileUploaded" 
        class="upload-button">Upload File</button>

        <!-- Display submit button when file is uploaded -->
        <button @click="submitFile" v-if="fileUploaded 
        && !fileProcessing" class="submit-button">
        <span v-if="!loading">Submit File</span>
        <span v-else>Loading...</span>
        </button>
    </div>

    <!-- Display download link when downloadUrl is available -->
    <div v-if="downloadUrl" class="download-link">
        <a :href="downloadUrl" download="samsung_regex_labeled_data.jsonl">
        <button class="download-button">Download Modified File</button>
        </a>
    </div>
  </div>
</template>

<script>
export default {  
  data() {
    return {
      file: null,
      fileUploaded: false,
      downloadUrl: null,
      loading: false,
      fileProcessing: false,
    }
  },
    methods: {
    openFileInput() {
      this.$refs.fileInput.click();
    },
    handleFileChange(event) {
      this.file = event.target.files[0];
      this.fileUploaded = true; // Set the flag to indicate file upload
    },
    handleFileDrop(event) {
      event.preventDefault();
      this.file = event.dataTransfer.files[0];
      this.fileUploaded = true; // Set the flag to indicate file upload
    },
    async submitFile() {
      if (!this.file) {
        alert("Please select a file.");
        return;
      }

      const formData = new FormData();
      formData.append("fileInput", this.file);

      try {
        this.loading = true;
        const response = await fetch("../v1/modify_file/", {
          method: "POST",
          body: formData,
          headers: {
            'X-CSRFToken': csrftoken,
          },
        });

        if (response.ok) {
          const responseData = await response.json(); // Assuming the response is JSON
          const fileContent = responseData.fileContent; // Accessing the file content

          // Convert the file content to a Blob object
          const blob = new Blob([fileContent], { type: 'application/json' });
          this.downloadUrl = URL.createObjectURL(blob);
        } else {
          console.error("Error processing the file.");
        }
      } catch (error) {
        console.error("An error occurred:", error);
      } finally {
        this.loading = false;
      }
    },
  },

}

// CODE FOR REGEX START
const csrftoken = getCookie('csrftoken'); // Replace 'csrftoken' with the name of your CSRF token cookie

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

// CODE FOR REGEX END
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.file-upload-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
  margin-bottom: 20px;
}

.file-drop {
  border: 2px dashed #ccc;
  padding: 150px; /* Increased padding for a bigger contour */
  text-align: center;
  cursor: pointer;
  font-size: 18px; /* Increased font size */
}

.upload-button {
  margin-top: 20px;
  padding: 10px 20px; /* Adjust padding as needed */
  background-color: #007bff; /* Change background color */
  color: white; /* Text color */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px; /* Adjust font size */
}

.upload-button:hover {
  background-color: #0056b3; /* Change hover color */
}

.submit-button {
  margin-top: 20px;
  padding: 10px 20px; /* Adjust padding as needed */
  background-color: #007bff; /* Change background color */
  color: white; /* Text color */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px; /* Adjust font size */
}

.submit-button:hover {
  background-color: #0056b3; /* Change hover color */
}

.download-link {
  margin-top: 20px;
}

.download-button {
  padding: 10px 20px; /* Adjust padding as needed */
  background-color: #28a745; /* Change background color */
  color: white; /* Text color */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px; /* Adjust font size */
  margin-bottom: 20px;
}

.download-button:hover {
  background-color: #1e7e34; /* Change hover color */
}

.loading-animation {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px; /* Adjust the height as needed */
}

.loader {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}



</style>