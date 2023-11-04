<html>
<html lang="en">
<head>
        <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Start your development with Creative Design landing page.">
    <meta name="author" content="Devcrud">
    <title>Zipping | Watch store</title>

    <!-- font icons -->
    <link rel="stylesheet" href="assets/vendors/themify-icons/css/themify-icons.css">

    <!-- Bootstrap + Creative Design main styles -->
        <link rel="stylesheet" href="assets/css/creative-design.css">

</head>
<body data-spy="scroll" data-target=".navbar" data-offset="40" id="home">
    <!-- Page Header -->
    <header class="header header-mini"> 
      <div class="header-title">Work with Us</div> 
      <nav aria-label="breadcrumb">
         <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="index.php">Home</a></li>
            <li class="breadcrumb-item active" aria-current="page">Work with Us</li>
         </ol>
      </nav>
    </header> <!-- End Of Page Header -->

    <section id="work" class="text-center">
        <!-- container -->
        <div class="container">
            <h1>WORK WITH US</h1>
            <p class="mb-5">If you are interested in working with us, do not hesitate to send us your curriculum.<br> The application will only accept zip files, inside them there must be a pdf file containing your curriculum.</p>

            <?php
            if(isset($_POST['submit'])) {
              // Get the uploaded zip file
              $zipFile = $_FILES['zipFile']['tmp_name'];
              if ($_FILES["zipFile"]["size"] > 300000) {
                echo "<p>File size must be less than 300,000 bytes.</p>";
              } else {
                // Create an md5 hash of the zip file
                $fileHash = md5_file($zipFile);
                // Create a new directory for the extracted files
                $uploadDir = "uploads/$fileHash/";
		$tmpDir = sys_get_temp_dir();
                // Extract the files from the zip
                $zip = new ZipArchive;
                if ($zip->open($zipFile) === true) {
                  if ($zip->count() > 1) {
                  echo '<p>Please include a single PDF file in the archive.<p>';
                  } else {
                  // Get the name of the compressed file
                  $fileName = $zip->getNameIndex(0);
                  if (pathinfo($fileName, PATHINFO_EXTENSION) === "pdf") {
                    $uploadPath = $tmpDir.'/'.$uploadDir;
                    echo exec('7z e '.$zipFile. ' -o' .$uploadPath. '>/dev/null');
                    if (file_exists($uploadPath.$fileName)) {
                      mkdir($uploadDir);
                      rename($uploadPath.$fileName, $uploadDir.$fileName);
                    }
                    echo '<p>File successfully uploaded and unzipped, a staff member will review your resume as soon as possible. Make sure it has been uploaded correctly by accessing the following path:</p><a href="'.$uploadDir.$fileName.'">'.$uploadDir.$fileName.'</a>'.'</p>';
                  } else {
                    echo "<p>The unzipped file must have  a .pdf extension.</p>";
                  }
                 }
                } else {
                  echo "Error uploading file.";
                }

              }
            }
            ?>

            <!-- Submit File -->
            <form id="zip-form" enctype="multipart/form-data" method="post" action="upload.php">
              <div class="mb-3">
                <input type="file" class="form-control" name="zipFile" accept=".zip">
              </div>
              <button type="submit" class="btn btn-primary" name="submit">Upload</button>
            </form><!-- End submit file -->

        </div><!-- End of Container-->      
    </section><!-- End of Contact Section -->
    <!-- Section -->
    <section class="pb-0">
        <!-- Container -->
        <div class="container">
            <!-- Pre footer -->
            <div class="pre-footer">
                <ul class="list">
                    <li class="list-head">
                        <h6 class="font-weight-bold">ABOUT US</h6>
                    </li>
                    <li class="list-body">
                      <p>Zipping Co. is a company that is dedicated to producing high-quality watches that are both stylish and functional. We are constantly pushing the boundaries of what is possible with watch design and are known for their commitment to innovation and customer service.</p>  
                      <a href="#"><strong class="text-primary">Zipping</strong> <span class="text-dark">Watch Store</span></a>
                    </li>
                </ul>
                <ul class="list">
                    <li class="list-head">
                        <h6 class="font-weight-bold">USEFUL LINKS</h6>
                    </li>
                    <li class="list-body">
                        <div class="row">
                            <div class="col">
                                <a href="#">Link 1</a>
                                <a href="#">Link 2</a>
                                <a href="#">Link 3</a>
                                <a href="#">Link 4</a>
                            </div>
                            <div class="col">
                                <a href="#">Link 5</a>
                                <a href="#">Link 6</a>
                                <a href="#">Link 7</a>
                                <a href="#">Link 8</a>
                            </div>
                        </div>
                    </li>
                </ul>
                <ul class="list">
                    <li class="list-head">
                        <h6 class="font-weight-bold">CONTACT INFO</h6>
                    </li>
                    <li class="list-body">
                        <p>Contact us and we'll get back to you within 24 hours.</p>
                        <p><i class="ti-location-pin"></i> 12345 Fake ST NoWhere AB Country</p>
                        <p><i class="ti-email"></i>  info@website.com</p>
                        <div class="social-links">
                            <a href="javascript:void(0)" class="link"><i class="ti-facebook"></i></a>
                            <a href="javascript:void(0)" class="link"><i class="ti-twitter-alt"></i></a>
                            <a href="javascript:void(0)" class="link"><i class="ti-google"></i></a>
                            <a href="javascript:void(0)" class="link"><i class="ti-pinterest-alt"></i></a>
                            <a href="javascript:void(0)" class="link"><i class="ti-instagram"></i></a>
                            <a href="javascript:void(0)" class="link"><i class="ti-rss"></i></a>
                        </div>
                    </li>
                </ul> 
            </div><!-- End of Pre footer -->            

            <!-- foooter -->
            <footer class="footer">
                <p>Made by <a href="https://github.com/xdann1">xDaNN1</p>
            </footer><!-- End of Footer-->  
            
        </div><!--End of Container -->      
    </section><!-- End of Section -->


</body>
</html>


