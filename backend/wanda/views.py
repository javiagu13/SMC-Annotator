import os
import shutil
import subprocess
import tempfile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def modify_file(request):
    if request.method == 'POST' and request.FILES.get('fileInput'):
        uploaded_file = request.FILES['fileInput']

        # Save the uploaded file to a temporary location on the host
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            for chunk in uploaded_file.chunks():
                temp_file.write(chunk)
            temp_file_path = temp_file.name  # Store the path of the temp file

        # Define the paths inside the Docker container and on the host
        save_file = os.path.abspath('./wanda/data/Origin_SMC_5000-5099.csv')
        local_output_file = os.path.abspath('./wanda/data/Origin_SMC_5000-5099_doccano.jsonl')

        # Move the temporary file to the save_file location
        print(temp_file_path)
        print(save_file)
        shutil.move(temp_file_path, save_file)

        # Command and arguments as a list
        # Assuming smc_labeling.py takes save_file as input and outputs to local_output_file
        command = ["python", "./wanda/smc_labeling.py", save_file, local_output_file]

        # Run the command
        subprocess.run(command)

        # Read the modified file content from the host
        with open(local_output_file, 'r', encoding='utf-8') as modified_file:
            modified_content = modified_file.read()

        # Clean up the local output file
        os.remove(save_file)

        return JsonResponse({'fileContent': modified_content})
    else:
        return JsonResponse({'error': 'File upload failed.'}, status=400)