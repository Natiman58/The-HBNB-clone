$(document).ready(function() {

    // To check the status of the API; api/v1/status
    var apiUrl = "http://0.0.0.0:5001/api/v1/status"
    $.get(apiUrl, function(data) {
        if(data.status === 'OK') {
            $('#api_status').addClass('available')
        } else {
            $('#api_status').removeClass('available')
        }
    });

    // selected object IDs
    var selectedAmenities = [];
    var selectedStates = [];
    var selectedCities = [];

    $('input[type="checkbox"]').change(function() {
        var selectedCheckbox = $(this);
        var checkboxType = selectedCheckbox.attr('data-type');
        var itemId = selectedCheckbox.data('id');
        var itemName = selectedCheckbox.data('name');
        var isChecked = selectedCheckbox.is(':checked');

        if(checkboxType === 'amenity') {
            if (isChecked) {
                selectedAmenities.push(itemName);
            } else {
                var index = selectedAmenities.indexOf(itemName);
                if (index !== -1) {
                    selectedAmenities.splice(index, 1);
                }
            }
        } else if (checkboxType === 'state') {
            if (isChecked) {
                selectedStates.push(itemName);
            } else {
                var index = selectedStates.indexOf(itemName);
                if (index !== -1) {
                    selectedStates.splice(index, 1);
                }
            }
        } else if (checkboxType === 'city') {
            if (isChecked) {
                selectedCities.push(itemName);
            } else {
                var index = selectedCities.indexOf(itemName);
                if (index !== -1) {
                    selectedCities.splice(index, 1);
                }
            }
        }

        updateStatesHeader();
        updateCitiesHeader();
        updateAmenitiesHeader();
    });

    function updateStatesHeader() {
        var selectedLocations = []

        selectedStates.forEach(function (stateName) {
            selectedLocations.push(stateName);
        });

        //selectedCities.forEach(function (cityName) {
        //    selectedLocations.push('City:' + cityName);
        //});

        if (selectedLocations.length > 0 && selectedLocations.length < 4) {
            $('.locations h4').text(selectedLocations.join(', '));
          } else if (selectedLocations.length >= 4) {
            var truncatedText = selectedLocations.slice(0, 3).join(', ') + ' ...';
            $('.locations h4').text(truncatedText);
          } else {
            $('.locations h4').text('');
          }
    }

    // Updates the amenities h4 section
    function updateAmenitiesHeader() {
        var selectedAmenitiesHeader = [];

        selectedAmenities.forEach(function(amenityName) {
            selectedAmenitiesHeader.push(amenityName);
        });

        if (selectedAmenitiesHeader.length > 0 && selectedAmenitiesHeader.length < 4) {
            $('#amenities_header').text(selectedAmenitiesHeader.join(', '));
            console.log(selectedAmenitiesHeader);
        } else if (selectedAmenitiesHeader.length >= 4) {
            var truncatedText = selectedAmenitiesHeader.slice(0, 3).join(', ') + ' ...';
            $('#amenities_header').text(truncatedText);
        } else {
            $('#amenities_header').text('');
        }
    };

    // update cities header
    function updateCitiesHeader() {
        var selectedCitiesHeader = [];

        selectedCities.forEach(function(citiesName) {
            selectedCitiesHeader.push(citiesName)
        });
        if (selectedCitiesHeader.length > 0 && selectedCitiesHeader.length < 2) {
            $('h5').text(selectedCitiesHeader.join(', '));
        } else if (selectedCitiesHeader.length >= 2) {
            var truncatedText = selectedCitiesHeader.slice(0, 2).join(', ') + ' ...';
            $('h5').text(truncatedText);
        } else {
            $('h5').text('');
        }
    };


    // create an article for each place function
    function createPlaceArticle(place) {

        var article = $('<article></article>');

        // Place name
        var placeName = $('<div class="coustom_h2"></div>').append($('<h2></h2>').text(place.name));

        // Price by night
        var pricePerNight = $('<div class="price_by_night"></div>').append($('<div class="price"></div>').append($('<p></p>').text(place.price_by_night)));

        // information
        var information = $('<div class="information"></div>');

        // Max guest
        var maxGuests = $('<div class="max_guest"></div>').append($('<div class="info_text"></div>').text(place.max_guest +' '+ 'Guest' + (place.max_guest > 1 ? 's': '')));

        // number of rooms
        var numberOfRooms = $('<div class="number_rooms"></div">').append($('<div class="info_text"></div)').text(place.number_rooms + ' '+ 'Bedroom' + (place.number_rooms > 1 ? 's':'')));

        // number of bathrooms
        var numberOfBathRooms = $('<div class="number_bathrooms"></div>').append($('<div class="info_text"></div>').text(place.number_bathrooms +' '+ 'Bathroom' + (place.number_bathrooms > 1 ? 's':'')));

        information.append(maxGuests, numberOfRooms, numberOfBathRooms)

        // Description
        var description = $('<div class="description"></div>').append($('<p></p>').html(place.description));

        // Reviews
        var reviewsToggle = $('<span></span>').addClass('show-review-button').text('Show');
        var h2Reviews = $('<h2></h2>').text('Reviews: ')
        var reviewText = $('<div></div>').addClass('review-text').text('this is the lol review...lol')

        // the review section
        var reviews = $('<div class="reviews_section"></div>').append(h2Reviews, reviewsToggle, reviewText)

         // Hide the review dropdown content by default
        reviewText.hide();

        article.append(placeName, pricePerNight, information, description, reviews)

        return article;
};

    // Add click event listner to the show review button
    $(document).on('click', '.show-review-button', function() {
        var article = $(this).closest('article');
        var reviewSection = article.find('.review-text');

        // Toggle the visibility of dropdown content
        reviewSection.toggle();

        // Update the button text
        var buttonText = $(this).text();
        if (buttonText === 'Show') {
          $(this).text('Hide');
        } else {
          $(this).text('Show');
        }
      });

    // A function to send a POST request to places_search
    function searchPlaces(amenityIds, cityIds, stateIds) {

        var apiUrl = 'http://0.0.0.0:5001/api/v1/places_search/';

        // create the request payload with the list of checked amenities
        var requestData = {
            amenities: Array.from(amenityIds),
            cities: Array.from(cityIds),
            states: Array.from(stateIds)
        };

        // make the POST request
        $.ajax({
            url: apiUrl,
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(requestData)
        }).done(function(data){
            var placesSection = $('.places');

             // clear exisitng places excluding h1 header; Places
            placesSection.children().not('h1').remove();

            // create articles for each place
            if(Array.isArray(data)) {
                data.forEach(function(place){
                    var placeArticle = createPlaceArticle(place);
                    placesSection.append(placeArticle);
                });
            }
        }).fail(function(jqXHR, textStatus, errorThrown) {
            console.error('Request failed:', textStatus, errorThrown);
          });
    }

    // Search Button click to send a POST request
    $('.button').click(function() {
        // Get the list of checked amenities
        var checkedAmenities = $('.amenity-checkbox:checked');

        // Get the list of checked cities
        var checkedCities = $('.city-checkbox:checked');

        // Get the list of checked states
        var checkedStates = $('.state-checkbox:checked');

        // Extract the amenity IDs
        var amenityIds = new Set();
        checkedAmenities.each(function() {
            amenityIds.add($(this).data('id'));
        });

        // Extract the city IDs
        var cityIds = new Set();
        checkedCities.each(function() {
            cityIds.add($(this).data('id'));
        });

        // Extract the state IDs
        var stateIds = new Set();
        checkedStates.each(function() {
            stateIds.add($(this).data('id'));
        });

        // make the search request with list of checked amenities, cities and states
        searchPlaces(amenityIds, cityIds, stateIds);
    });
});
