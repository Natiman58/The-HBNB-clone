$(document).ready(function() {
    // To check the status of the API; api/v1/status
    var apiUrl = "http://0.0.0.0:5001/api/v1/status"

    $.get(apiUrl, function(data) {
        if(data.status === 'OK') {
            $('#api_status').addClass('available')
        } else {
            console.log(data)
            $('#api_status').removeClass('available')
        }
    });

    // Updates the amenities based on the selection of the user checkbox
    var selectedAmenities = [];

    $('input[type="checkbox"]').change(function() {
      var selectedCheckbox = $(this);
      var amenityName = selectedCheckbox.data('name');
      var isChecked = selectedCheckbox.is(':checked');

      if (isChecked) {
        selectedAmenities.push(amenityName);
      } else {
        var index = selectedAmenities.indexOf(amenityName);
        if (index !== -1) {
          selectedAmenities.splice(index, 1);
        }
      }

      if (selectedAmenities.length > 0 && selectedAmenities.length < 4) {
        $('.amenities h4').text(selectedAmenities.join(', '));
      } else if (selectedAmenities.length >= 4) {
        var truncatedText = selectedAmenities.slice(0, 3).join(', ') + ' ...';
        $('.amenities h4').text(truncatedText);
      } else {
        $('.amenities h4').text('');
      }
    });

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


      article.append(placeName, pricePerNight, information, description)

      return article;
    }

    // A function to send a POST request to places_search
    function searchPlaces(amenities) {

        console.log(amenities)
        var apiUrl = 'http://0.0.0.0:5001/api/v1/places_search/';

        // create the request payload with the list of checked amenities
        var requestData = {
            amenities: Array.from(amenities)
        };

        // make the POST request
        $.ajax({
            url: apiUrl,
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(requestData)
        }).done(function(data){
            var placesSection = $('.places');

             //clear exisitng places excluding h1 header; Places
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

    // Button click to send a POST request
    $('.button').click(function() {
        // Get the list of checked amenities
        var checkedAmenities = $('.amenity-checkbox:checked');
        //console.log(checkedAmenities)

        // Extract the amenity IDs
        var amenityIds = new Set();
        checkedAmenities.each(function() {
            amenityIds.add($(this).data('id'));
        });
        // make the search request with list of checked amenities
        searchPlaces(amenityIds);
    });
});
