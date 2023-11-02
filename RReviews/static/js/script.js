(function ($) {
  "use strict";

  //Hide Loading Box (Preloader)
  function handlePreloader() {
    if ($(".loader-wrap").length) {
      $(".loader-wrap").delay(1000).fadeOut(500);
    }
    TweenMax.to($(".loader-wrap .overlay"), 1.2, {
      force3D: true,
      left: "100%",
      ease: Expo.easeInOut,
    });
  }

  if ($(".preloader-close").length) {
    $(".preloader-close").on("click", function () {
      $(".loader-wrap").delay(200).fadeOut(500);
    });
  }

  //Update Header Style and Scroll to Top
  function headerStyle() {
    if ($(".main-header").length) {
      var windowpos = $(window).scrollTop();
      var siteHeader = $(".main-header");
      var scrollLink = $(".scroll-top");
      if (windowpos >= 110) {
        siteHeader.addClass("fixed-header");
        scrollLink.addClass("open");
      } else {
        siteHeader.removeClass("fixed-header");
        scrollLink.removeClass("open");
      }
    }
  }

  headerStyle();

  //Submenu Dropdown Toggle
  if ($(".main-header li.dropdown ul").length) {
    $(".main-header .navigation li.dropdown").append(
      '<div class="dropdown-btn"><span class="fas fa-angle-down"></span></div>'
    );
  }

  //Mobile Nav Hide Show
  if ($(".mobile-menu").length) {
    $(".mobile-menu .menu-box").mCustomScrollbar();

    var mobileMenuContent = $(".main-header .menu-area .main-menu").html();
    $(".mobile-menu .menu-box .menu-outer").append(mobileMenuContent);
    $(".sticky-header .main-menu").append(mobileMenuContent);

    //Dropdown Button
    $(".mobile-menu li.dropdown .dropdown-btn").on("click", function () {
      $(this).toggleClass("open");
      $(this).prev("ul").slideToggle(500);
    });
    //Dropdown Button
    $(".mobile-menu li.dropdown .dropdown-btn").on("click", function () {
      $(this).prev(".megamenu").slideToggle(900);
    });
    //Menu Toggle Btn
    $(".mobile-nav-toggler").on("click", function () {
      $("body").addClass("mobile-menu-visible");
    });

    //Menu Toggle Btn
    $(".mobile-menu .menu-backdrop,.mobile-menu .close-btn").on(
      "click",
      function () {
        $("body").removeClass("mobile-menu-visible");
      }
    );
  }

  //Side Nav Hide Show
  if ($(".side-menu").length) {
    $(".side-menu .menu-box").mCustomScrollbar();

    var mobileMenuContent = $(".main-header .menu-area .main-menu").html();
    $(".side-menu .menu-box .menu-outer").append(mobileMenuContent);

    //Dropdown Button
    $(".side-menu li.dropdown .dropdown-btn").on("click", function () {
      $(this).toggleClass("open");
      $(this).prev("ul").slideToggle(500);
    });
    //Dropdown Button
    $(".side-menu li.dropdown .dropdown-btn").on("click", function () {
      $(this).prev(".megamenu").slideToggle(900);
    });
  }

  // Scroll to a Specific Div
  if ($(".scroll-to-target").length) {
    $(".scroll-to-target").on("click", function () {
      var target = $(this).attr("data-target");
      // animate
      $("html, body").animate(
        {
          scrollTop: $(target).offset().top,
        },
        1000
      );
    });
  }

  // Elements Animation
  if ($(".wow").length) {
    var wow = new WOW({
      mobile: false,
    });
    wow.init();
  }

  //Contact Form Validation
  if ($("#contact-form").length) {
    $("#contact-form").validate({
      rules: {
        username: {
          required: true,
        },
        email: {
          required: true,
          email: true,
        },
        phone: {
          required: true,
        },
        subject: {
          required: true,
        },
        message: {
          required: true,
        },
      },
    });
  }

  //Fact Counter + Text Count
  if ($(".count-box").length) {
    $(".count-box").appear(
      function () {
        var $t = $(this),
          n = $t.find(".count-text").attr("data-stop"),
          r = parseInt($t.find(".count-text").attr("data-speed"), 10);

        if (!$t.hasClass("counted")) {
          $t.addClass("counted");
          $({
            countNum: $t.find(".count-text").text(),
          }).animate(
            {
              countNum: n,
            },
            {
              duration: r,
              easing: "linear",
              step: function () {
                $t.find(".count-text").text(Math.floor(this.countNum));
              },
              complete: function () {
                $t.find(".count-text").text(this.countNum);
              },
            }
          );
        }
      },
      { accY: 0 }
    );
  }

  //LightBox / Fancybox
  if ($(".lightbox-image").length) {
    $(".lightbox-image").fancybox({
      openEffect: "fade",
      closeEffect: "fade",
      helpers: {
        media: {},
      },
    });
  }

  //Tabs Box
  if ($(".tabs-box").length) {
    $(".tabs-box .tab-buttons .tab-btn").on("click", function (e) {
      e.preventDefault();
      var target = $($(this).attr("data-tab"));

      if ($(target).is(":visible")) {
        return false;
      } else {
        target
          .parents(".tabs-box")
          .find(".tab-buttons")
          .find(".tab-btn")
          .removeClass("active-btn");
        $(this).addClass("active-btn");
        target
          .parents(".tabs-box")
          .find(".tabs-content")
          .find(".tab")
          .fadeOut(0);
        target
          .parents(".tabs-box")
          .find(".tabs-content")
          .find(".tab")
          .removeClass("active-tab");
        $(target).fadeIn(300);
        $(target).addClass("active-tab");
      }
    });
  }

  //Accordion Box
  if ($(".accordion-box").length) {
    $(".accordion-box").on("click", ".acc-btn", function () {
      var outerBox = $(this).parents(".accordion-box");
      var target = $(this).parents(".accordion");

      if ($(this).hasClass("active") !== true) {
        $(outerBox).find(".accordion .acc-btn").removeClass("active");
      }

      if ($(this).next(".acc-content").is(":visible")) {
        return false;
      } else {
        $(this).addClass("active");
        $(outerBox).children(".accordion").removeClass("active-block");
        $(outerBox).find(".accordion").children(".acc-content").slideUp(300);
        target.addClass("active-block");
        $(this).next(".acc-content").slideDown(300);
      }
    });
  }

  // banner-carousel
  if ($(".banner-carousel").length) {
    $(".banner-carousel").owlCarousel({
      loop: true,
      margin: 0,
      nav: true,
      animateOut: "fadeOut",
      animateIn: "fadeIn",
      active: true,
      smartSpeed: 1000,
      autoplay: 6000,
      navText: [
        '<span class="fa fa-angle-left"></span>',
        '<span class="fa fa-angle-right"></span>',
      ],
      responsive: {
        0: {
          items: 1,
        },
        600: {
          items: 1,
        },
        800: {
          items: 1,
        },
        1024: {
          items: 1,
        },
      },
    });
  }

  // project-carousel-2
  if ($(".project-carousel-2").length) {
    $(".project-carousel-2").owlCarousel({
      loop: true,
      margin: 0,
      nav: true,
      animateOut: "fadeOut",
      animateIn: "fadeIn",
      active: true,
      smartSpeed: 1000,
      autoplay: 6000,
      navText: [
        '<span class="fa fa-angle-left"></span>',
        '<span class="fa fa-angle-right"></span>',
      ],
      responsive: {
        0: {
          items: 1,
        },
        600: {
          items: 1,
        },
        800: {
          items: 1,
        },
        1024: {
          items: 1,
        },
      },
    });
  }

  // sidebar-carousel
  if ($(".sidebar-carousel").length) {
    $(".sidebar-carousel").owlCarousel({
      loop: true,
      margin: 30,
      nav: true,
      smartSpeed: 500,
      autoplay: 1000,
      navText: [
        '<span class="fas fa-arrow-left"></span>',
        '<span class="fas fa-arrow-right"></span>',
      ],
      responsive: {
        0: {
          items: 1,
        },
        600: {
          items: 1,
        },
        800: {
          items: 1,
        },
        1024: {
          items: 1,
        },
      },
    });
  }

  // news-carousel
  if ($(".news-carousel").length) {
    $(".news-carousel").owlCarousel({
      loop: true,
      margin: 30,
      nav: true,
      smartSpeed: 500,
      autoplay: 1000,
      navText: [
        '<span class="fas fa-angle-left"></span>',
        '<span class="fas fa-angle-right"></span>',
      ],
      responsive: {
        0: {
          items: 1,
        },
        600: {
          items: 1,
        },
        800: {
          items: 1,
        },
        1024: {
          items: 1,
        },
      },
    });
  }

  //three-item-carousel
  if ($(".three-item-carousel").length) {
    $(".three-item-carousel").owlCarousel({
      loop: true,
      margin: 30,
      nav: true,
      smartSpeed: 1000,
      autoplay: 500,
      navText: [
        '<span class="fas fa-arrow-left"></span>',
        '<span class="fas fa-arrow-right"></span>',
      ],
      responsive: {
        0: {
          items: 1,
        },
        480: {
          items: 1,
        },
        600: {
          items: 2,
        },
        800: {
          items: 2,
        },
        1024: {
          items: 3,
        },
      },
    });
  }

  //project-carousel
  if ($(".project-carousel").length) {
    $(".project-carousel").owlCarousel({
      loop: true,
      margin: 0,
      nav: true,
      smartSpeed: 1000,
      autoplay: 500,
      navText: [
        '<span class="fas fa-arrow-left"></span>',
        '<span class="fas fa-arrow-right"></span>',
      ],
      responsive: {
        0: {
          items: 1,
        },
        480: {
          items: 1,
        },
        600: {
          items: 2,
        },
        800: {
          items: 2,
        },
        1024: {
          items: 3,
        },
      },
    });
  }

  // Four Item Carousel
  if ($(".four-item-carousel").length) {
    $(".four-item-carousel").owlCarousel({
      loop: true,
      margin: 30,
      nav: true,
      autoHeight: true,
      smartSpeed: 500,
      autoplay: 5000,
      navText: [
        '<span class="fas fa-angle-left"></span>',
        '<span class="fas fa-angle-right"></span>',
      ],
      responsive: {
        0: {
          items: 1,
        },
        600: {
          items: 2,
        },
        800: {
          items: 3,
        },
        1024: {
          items: 3,
        },
        1200: {
          items: 4,
        },
      },
    });
  }

  //Client Testimonial Carousel
  if (
    $(".client-testimonial-carousel").length &&
    $(".client-thumbs-carousel").length
  ) {
    var $sync3 = $(".client-testimonial-carousel"),
      $sync4 = $(".client-thumbs-carousel"),
      flag = false,
      duration = 500;

    $sync3
      .owlCarousel({
        loop: true,
        items: 1,
        margin: 0,
        nav: true,
        navText: [
          '<span class="fa fa-angle-left"></span>',
          '<span class="fa fa-angle-right"></span>',
        ],
        dots: false,
        autoplay: true,
        autoplayTimeout: 5000,
      })
      .on("changed.owl.carousel", function (e) {
        if (!flag) {
          flag = false;
          $sync4.trigger("to.owl.carousel", [e.item.index, duration, true]);
          flag = false;
        }
      });

    $sync4
      .owlCarousel({
        loop: true,
        margin: 10,
        items: 1,
        nav: false,
        navText: [
          '<span class="icon fa fa-long-arrow-left"></span>',
          '<span class="icon fa fa-long-arrow-right"></span>',
        ],
        dots: true,
        center: false,
        autoplay: true,
        autoplayTimeout: 5000,
        responsive: {
          0: {
            items: 1,
            autoWidth: false,
          },
          400: {
            items: 1,
            autoWidth: false,
          },
          600: {
            items: 1,
            autoWidth: false,
          },
          1000: {
            items: 1,
            autoWidth: false,
          },
          1200: {
            items: 1,
            autoWidth: false,
          },
        },
      })

      .on("click", ".owl-item", function () {
        $sync3.trigger("to.owl.carousel", [$(this).index(), duration, true]);
      })
      .on("changed.owl.carousel", function (e) {
        if (!flag) {
          flag = true;
          $sync3.trigger("to.owl.carousel", [e.item.index, duration, true]);
          flag = false;
        }
      });
  }

  //two-column-carousel
  if ($(".two-column-carousel").length) {
    $(".two-column-carousel").owlCarousel({
      loop: true,
      margin: 30,
      nav: true,
      smartSpeed: 3000,
      autoplay: 4000,
      navText: [
        '<span class="fa fa-caret-left"></span>',
        '<span class="fa fa-caret-right"></span>',
      ],
      responsive: {
        0: {
          items: 1,
        },
        480: {
          items: 1,
        },
        600: {
          items: 1,
        },
        800: {
          items: 2,
        },
        1024: {
          items: 2,
        },
      },
    });
  }

  // clients-carousel
  if ($(".clients-carousel").length) {
    $(".clients-carousel").owlCarousel({
      loop: true,
      margin: 30,
      nav: false,
      smartSpeed: 3000,
      autoplay: true,
      navText: [
        '<span class="flaticon-left"></span>',
        '<span class="flaticon-right"></span>',
      ],
      responsive: {
        0: {
          items: 1,
        },
        480: {
          items: 2,
        },
        600: {
          items: 3,
        },
        800: {
          items: 4,
        },
        1200: {
          items: 5,
        },
      },
    });
  }

  //Add One Page nav
  if ($(".scroll-nav").length) {
    $(".scroll-nav").onePageNav();
  }

  //Progress Bar
  if ($(".count-bar").length) {
    $(".count-bar").appear(
      function () {
        var el = $(this);
        var percent = el.data("percent");
        $(el).css("width", percent).addClass("counted");
      },
      { accY: -50 }
    );
  }

  //Search Popup
  if ($("#search-popup").length) {
    //Show Popup
    $(".search-toggler").on("click", function () {
      $("#search-popup").addClass("popup-visible");
    });
    $(document).keydown(function (e) {
      if (e.keyCode === 27) {
        $("#search-popup").removeClass("popup-visible");
      }
    });
    //Hide Popup
    $(".close-search,.search-popup .overlay-layer").on("click", function () {
      $("#search-popup").removeClass("popup-visible");
    });
  }

  // page direction
  function directionswitch() {
    if ($(".page_direction").length) {
      $(".direction_switch button").on("click", function () {
        $("body").toggleClass(function () {
          return $(this).is(".rtl, .ltr") ? "rtl ltr" : "rtl";
        });
      });
    }
  }

  // pieChart RoundCircle
  function expertizeRoundCircle() {
    var rounderContainer = $(".piechart");
    if (rounderContainer.length) {
      rounderContainer.each(function () {
        var Self = $(this);
        var value = Self.data("value");
        var size = Self.parent().width();
        var color = Self.data("fg-color");

        Self.find("span").each(function () {
          var expertCount = $(this);
          expertCount.appear(function () {
            expertCount.countTo({
              from: 1,
              to: value * 100,
              speed: 3000,
            });
          });
        });
        Self.appear(function () {
          Self.circleProgress({
            value: value,
            size: 170,
            thickness: 20,
            emptyFill: "#e7f0f8",
            animation: {
              duration: 3000,
            },
            fill: {
              color: color,
            },
          });
        });
      });
    }
  }

  $(document).ready(function () {
    $("select:not(.ignore)").niceSelect();
  });

  //Sortable Masonary with Filters
  function enableMasonry() {
    if ($(".sortable-masonry").length) {
      var winDow = $(window);
      // Needed variables
      var $container = $(".sortable-masonry .items-container");
      var $filter = $(".filter-btns");

      $container.isotope({
        filter: "*",
        masonry: {
          columnWidth: ".masonry-item.small-column",
        },
        animationOptions: {
          duration: 500,
          easing: "linear",
        },
      });

      // Isotope Filter
      $filter.find("li").on("click", function () {
        var selector = $(this).attr("data-filter");

        try {
          $container.isotope({
            filter: selector,
            animationOptions: {
              duration: 500,
              easing: "linear",
              queue: false,
            },
          });
        } catch (err) {}
        return false;
      });

      winDow.on("resize", function () {
        var selector = $filter.find("li.active").attr("data-filter");

        $container.isotope({
          filter: selector,
          animationOptions: {
            duration: 500,
            easing: "linear",
            queue: false,
          },
        });
      });

      var filterItemA = $(".filter-btns li");

      filterItemA.on("click", function () {
        var $this = $(this);
        if (!$this.hasClass("active")) {
          filterItemA.removeClass("active");
          $this.addClass("active");
        }
      });
    }
  }

  enableMasonry();

  /*	=========================================================================
	When document is Scrollig, do
	========================================================================== */

  jQuery(document).on("ready", function () {
    (function ($) {
      // add your functions
      directionswitch();
    })(jQuery);
  });

  /* ==========================================================================
   When document is Scrollig, do
   ========================================================================== */

  $(window).on("scroll", function () {
    headerStyle();
  });

  /* ==========================================================================
   When document is loaded, do
   ========================================================================== */

  $(window).on("load", function () {
    handlePreloader();
    expertizeRoundCircle();
    enableMasonry();
  });
})(window.jQuery);


// // Initialize and add the map
// function initMap() {
//   // The location of Uluru
//   const uluru = { lat: -25.344, lng: 131.031 };
//   // The map, centered at Uluru
//   const map = new google.maps.Map(document.getElementById("map"), {
//     zoom: 4,
//     center: uluru,
//   });
//   // The marker, positioned at Uluru
//   const marker = new google.maps.Marker({
//     position: uluru,
//     map: map,
//   });
// }

function initialize() {

	var mapOptions, map, marker, searchBox, city,
		infoWindow = '',
		addressEl = document.querySelector( '#map-search' ),
		latEl = document.querySelector( '.latitude' ),
		longEl = document.querySelector( '.longitude' ),
		element = document.getElementById( 'map' );
	city = document.querySelector( '.reg-input-city' );

	mapOptions = {
		// How far the maps zooms in.
		zoom: 4,
		// Current Lat and Long position of the pin/
		center: new google.maps.LatLng( -25.344, 131.031 ),
		// center : {
		// 	lat: -34.397,
		// 	lng: 150.644
		// },
		disableDefaultUI: false, // Disables the controls like zoom control on the map if set to true
		scrollWheel: true, // If set to false disables the scrolling on the map.
		draggable: true, // If set to false , you cannot move the map around.
		// mapTypeId: google.maps.MapTypeId.HYBRID, // If set to HYBRID its between sat and ROADMAP, Can be set to SATELLITE as well.
		// maxZoom: 11, // Wont allow you to zoom more than this
		// minZoom: 9  // Wont allow you to go more up.

	};

	/**
	 * Creates the map using google function google.maps.Map() by passing the id of canvas and
	 * mapOptions object that we just created above as its parameters.
	 *
	 */
	// Create an object map with the constructor function Map()
	map = new google.maps.Map( element, mapOptions ); // Till this like of code it loads up the map.

	/**
	 * Creates the marker on the map
	 *
	 */
	marker = new google.maps.Marker({
		position: mapOptions.center,
		map: map,
		// icon: 'http://pngimages.net/sites/default/files/google-maps-png-image-70164.png',
		draggable: true
	});

	/**
	 * Creates a search box
	 */
	searchBox = new google.maps.places.SearchBox( addressEl );

	/**
	 * When the place is changed on search box, it takes the marker to the searched location.
	 */
	google.maps.event.addListener( searchBox, 'places_changed', function () {
		var places = searchBox.getPlaces(),
			bounds = new google.maps.LatLngBounds(),
			i, place, lat, long, resultArray,
			addresss = places[0].formatted_address;

		for( i = 0; place = places[i]; i++ ) {
			bounds.extend( place.geometry.location );
			marker.setPosition( place.geometry.location );  // Set marker position new.
		}

		map.fitBounds( bounds );  // Fit to the bound
		map.setZoom( 15 ); // This function sets the zoom to 15, meaning zooms to level 15.
		// console.log( map.getZoom() );

		lat = marker.getPosition().lat();
		long = marker.getPosition().lng();
		latEl.value = lat;
		longEl.value = long;

		resultArray =  places[0].address_components;

		// Get the city and set the city input value to the one selected
		for( var i = 0; i < resultArray.length; i++ ) {
			if ( resultArray[ i ].types[0] && 'administrative_area_level_2' === resultArray[ i ].types[0] ) {
				citi = resultArray[ i ].long_name;
				city.value = citi;
			}
		}

		// Closes the previous info window if it already exists
		if ( infoWindow ) {
			infoWindow.close();
		}
		/**
		 * Creates the info Window at the top of the marker
		 */
		infoWindow = new google.maps.InfoWindow({
			content: addresss
		});

		infoWindow.open( map, marker );
	} );


	/**
	 * Finds the new position of the marker when the marker is dragged.
	 */
	google.maps.event.addListener( marker, "dragend", function ( event ) {
		var lat, long, address, resultArray, citi;

		console.log( 'i am dragged' );
		lat = marker.getPosition().lat();
		long = marker.getPosition().lng();

		var geocoder = new google.maps.Geocoder();
		geocoder.geocode( { latLng: marker.getPosition() }, function ( result, status ) {
			if ( 'OK' === status ) {  // This line can also be written like if ( status == google.maps.GeocoderStatus.OK ) {
				address = result[0].formatted_address;
				resultArray =  result[0].address_components;

				// Get the city and set the city input value to the one selected
				for( var i = 0; i < resultArray.length; i++ ) {
					if ( resultArray[ i ].types[0] && 'administrative_area_level_2' === resultArray[ i ].types[0] ) {
						citi = resultArray[ i ].long_name;
						console.log( citi );
						city.value = citi;
					}
				}
				addressEl.value = address;
				latEl.value = lat;
				longEl.value = long;

			} else {
				console.log( 'Geocode was not successful for the following reason: ' + status );
			}

			// Closes the previous info window if it already exists
			if ( infoWindow ) {
				infoWindow.close();
			}

			/**
			 * Creates the info Window at the top of the marker
			 */
			infoWindow = new google.maps.InfoWindow({
				content: address
			});

			infoWindow.open( map, marker );
		} );
	});


}

//--------------------------------------------------------------
// JS for Home Page Tiles Menu (International Cuisine, etc)

let intercusine = document.getElementById("intcuis");
let favfoodtile = document.getElementById("favf");
let fastfoodtile = document.getElementById("fastf");
let orbrowse = document.getElementById('orbrowse');
let btom = document.getElementById('btom');
let tileshome = document.getElementsByClassName('mainmenu')[0];
let incusinetiles = document.getElementsByClassName('int-cuisines')[0];
let favfoodtiles = document.getElementsByClassName('fav-food')[0];
let fastfoodtiles = document.getElementsByClassName('fast-food')[0];

intercusine.addEventListener("click", function() {
  orbrowse.style.display="none";
  btom.style.display="flex";
  tileshome.style.display='none';
  incusinetiles.style.display='flex';
})

fastfoodtile.addEventListener("click", function() {
  orbrowse.style.display="none";
  btom.style.display="flex";
  tileshome.style.display='none';
  fastfoodtiles.style.display='flex';
})

favfoodtile.addEventListener("click", function() {
  orbrowse.style.display="none";
  btom.style.display="flex";
  tileshome.style.display='none';
  favfoodtiles.style.display='flex';
})

btom.addEventListener('click', () => {
  orbrowse.style.display="flex";
  btom.style.display="none";
  tileshome.style.display='flex';
  incusinetiles.style.display='none';
  favfoodtiles.style.display='none';
  fastfoodtiles.style.display='none';



})

//--------------------------------------------------------------

// JS for changing Menu Title on the Menu Display page

// var mp = document.getElementsByClassName("menutabs");
// console.log(mp)
// var mtype = mp[0].getElementsByTagName("li");
// for (i = 0; i < mtype.length; i++) {
//   let titletext = mtype[i].innerHTML;
//   console.log(titletext);
//   mtype[i].addEventListener("click", () => {
    
//     document.getElementById('menu-title').innerHTML=titletext;    
  
//   });

// }