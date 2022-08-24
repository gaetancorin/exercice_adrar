<!-- HEADER DE LA PAGE INSERT_INPUTS -->

<?php $stylesheets[] = 'src/lib/css/layout/header_app_asides.css'; ?>

<?php ob_start(); ?>

    <!------ HEADER TOP--->
    <header>
        <div class="header_top">
            <h2 class="aquarium_name">Aquarium 1</h2>
            <p class="logo">logo</p>
            <div class="hamburger_conteneur">
                <input type="checkbox" name="" id="">
                <ul class="conteneur_aside_hamb">                
                    <li><a class="a_aside_hamb" href="https://www.google.com/">
                            <img class="img_fish_hamb" src="./image_site/poisson_burger_1.svg">
                            Aquarium 1       
                        </a></li>
                    <li><a class="a_aside_hamb" href="https://www.google.com/">
                            <img class="img_fish_hamb" src="./image_site/poisson_burger_2.svg">
                            Aquarium 2       
                        </a></li>                
                    <li><a class="a_aside_hamb" href="https://www.google.com/">
                            <img class="img_fish_hamb" src="./image_site/poisson_burger_3.svg">
                            Créer nouvel aquarium      
                        </a></li>                
                    <li><a class="a_aside_hamb" href="https://www.google.com/">
                            <img class="img_fish_hamb" src="./image_site/poisson_burger_4.svg">
                            Changer nom de l' aquarium       
                        </a></li>                
                    <li><a class="a_aside_hamb" href="https://www.google.com/">
                            <img class="img_fish_hamb" src="./image_site/poisson_burger_5.svg">
                            Supprimer un aquarium       
                        </a></li>                
                    <li><a class="a_aside_hamb" href="https://www.google.com/">
                            <img class="img_fish_hamb" src="./image_site/poisson_burger_6.svg">
                            Déconnection       
                        </a></li>   
                </ul>
                <img class="hamburger_header" src="./image_site/parametre_header.svg">
            </div>
        </div>
    </header>

    <!-- RESPONSIVE DES ASIDE PAR GRID-->
    <section id="responsive_des_aside">

        <!-- ASIDE GAUCHE HAMBURGER-->
        <aside id="aside_gauche_hamb">
            <ul class="ul_aside_hamb">
                
                <li>
                    <a class="a_aside_hamb" href="https://www.google.com/">
                        <img class="img_fish_hamb" src="./image_site/poisson_burger_1.svg">
                        Aquarium 1       
                    </a>
                </li>
                <li>
                    <a class="a_aside_hamb" href="https://www.google.com/">
                        <img class="img_fish_hamb" src="./image_site/poisson_burger_2.svg">
                        Aquarium 2       
                    </a>
                </li>                <li>
                    <a class="a_aside_hamb" href="https://www.google.com/">
                        <img class="img_fish_hamb" src="./image_site/poisson_burger_3.svg">
                        Créer nouvel aquarium      
                    </a>
                </li>                <li>
                    <a class="a_aside_hamb" href="https://www.google.com/">
                        <img class="img_fish_hamb" src="./image_site/poisson_burger_4.svg">
                        Changer nom de l' aquarium       
                    </a>
                </li>                <li>
                    <a class="a_aside_hamb" href="https://www.google.com/">
                        <img class="img_fish_hamb" src="./image_site/poisson_burger_5.svg">
                        Supprimer un aquarium       
                    </a>
                </li>                <li>
                    <a class="a_aside_hamb" href="https://www.google.com/">
                        <img class="img_fish_hamb" src="./image_site/poisson_burger_6.svg">
                        Déconnection       
                    </a>
                </li>

            </ul>
        </aside>

        <!-- ASIDE DROITE PUBLICITE-->
        <aside id="aside_droite_pub">
            <div class="box_publicite">
                
                <div class="zone_titre_top_pub">
                    <p class="text_titre_top_pub">Liens pratiques</p>
                </div>

                <a class="lien_pub" href="https://www.amazon.fr/">
                    <img class="img_1_aside_pub" src="./image_site/image_malette_1_transparent.png" alt="mallette de test a goutte JBl lien Amazon">
                </a>

                <a  class="lien_pub" href="https://www.amazon.fr/">
                    <img class="img_2_aside_pub" src="./image_site/image_malette_2_transparent.png" alt="mallette de test a goutte JBl lien Amazon">
                </a>
  
            </div>
        </aside>


        <!----  SECTION CENTRALE  ---->
        <section class="section_centrale">

            <?= $content ?>

        </section>
    </section>



<?php $content = ob_get_clean(); ?>

<?php require('templates/layout/doctype_head.php') ?>