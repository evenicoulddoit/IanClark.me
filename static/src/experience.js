(function($) {
  "use strict";

  var experience = {
    init: function() {
      this.extract_dom();
      this.events();
    },

    /**
     * Retrieve and store all valid jQuery elements from the DOM
     */
    extract_dom: function() {

      // Technology elements
      this.$wrapperTech = $("#experience-technologies-inside");
      this.$elemsTech = $(".technology-story", this.$wrapperTech);
      this.$btnCloseTech = $("#tech-story-close");
      this.$currentTech = this.$prevTech = this.$nextTech = $();

      // Timeline elements
      this.$wrapperTimeline = $("#experience-timeline-inside");
      this.wrapperTimelineClass = this.$wrapperTimeline.attr("class");
      this.$elemsTimeline = $(".timeline-period", this.$wrapperTimeline);
    },

    /**
     * Show a specific technology story
     */
    tech_show: function($elm) {

      // Ignore subsequent clicks on the same story
      if(!this.$currentTech.is($elm)) {

        // If a tech wasn't active before this, initialise keyboard events
        if(this.active != "tech") {
          this.active = "tech";
          this.modals_reset();
          this.$wrapperTech.addClass("story");
          this._init_modal_keyevents(this.tech_set_prev_active,
                                     this.tech_set_next_active,
                                     this.tech_close);
        }

        // Remove classes set on previous active & navigation stories
        this.$currentTech.removeClass("active story-visible");
        this.$prevTech.add(this.$nextTech).removeClass("navigate prev next story-visible");

        // Set the new current tech and use this to calculate the previous / next ones
        this.$currentTech = $elm.addClass("active story-visible");

        // Calculate the next and previous stories and put them in the navigation
        this.$prevTech = this._get_prev_or_last(this.$currentTech, this.$elemsTech);
        this.$prevTech.addClass("navigate prev story-visible");

        this.$nextTech = this._get_next_or_first(this.$currentTech, this.$elemsTech);
        this.$nextTech.addClass("navigate next story-visible");

        // Start a fresh time out to add the loaded class to the wrapper
        clearTimeout(this.loadedTimeout);
        this.$wrapperTech.removeClass("loaded");
        this.loadedTimeout = setTimeout($.proxy(this.tech_set_loaded, this), 500);
      }
    },

    /**
     * Set the current technology story as loaded (When CSS animations are complete)
     */
    tech_set_loaded: function() {
      this.$wrapperTech.addClass("loaded");
    },

    /**
     * Make previous technology story active
     */
    tech_set_prev_active: function() {
      this.tech_show(this.$prevTech);
    },

    /**
     * Make next technology story active
     */
    tech_set_next_active: function() {
      this.tech_show(this.$nextTech);
    },

    /**
     * Close the active technology story, returning to grid
     */
    tech_close: function() {
      this.$wrapperTech.removeClass("story loaded");
      this.$elemsTech.attr("class", "technology-story");
      this.$currentTech = $();
      this._modal_close();
    },

    /**
     * Show a timeline event
     */
    timeline_show: function($period) {

      // Get the date part of the ID
      var period = $period.attr("id").split("-").slice(1).join("-");

      // If timeline wasn't active before this, initialise keyboard events
      if(this.active != "timeline") {
        this.active = "timeline";
        this.modals_reset();
        this._init_modal_keyevents(this.timeline_set_prev_active,
                                   this.timeline_set_next_active,
                                   this.timeline_close);
      }

      this.$currentTimeline = $period;
      this.$wrapperTimeline.attr("class", this.wrapperTimelineClass +
                                          " active active-" + period);
    },

    /**
     * Set the previous timeline event
     */
    timeline_set_prev_active: function() {
      var $prev = this._get_prev_or_last(this.$currentTimeline, this.$elemsTimeline)
      this.timeline_show($prev);
    },

    /**
     * Set the next timeline event
     */
    timeline_set_next_active: function() {
      var $next = this._get_next_or_first(this.$currentTimeline, this.$elemsTimeline)
      this.timeline_show($next);
    },

    /**
     * Close all timeline events
     */
    timeline_close: function() {
      this.$wrapperTimeline.attr("class", this.wrapperTimelineClass);
      this._modal_close();
    },

    /**
     * Reset all modals to their initial state
     */
    modals_reset: function() {
      this.tech_close();
      this.timeline_close();
    },

    /**
     * Always events for when closing a modal
     */
    _modal_close: function() {
      this._disable_modal_keyevents();
      delete this.active;
    },

    /**
     * Track key events when a modal is active
     */
    _init_modal_keyevents: function(fPrev, fNext, fClose) {
      var _this = this;

      $(window).off("keydown").on("keydown", function(e) {
        switch(e.keyCode) {
          // left
          case 37:
            fPrev.apply(_this);
            break;
          // right
          case 39:
            fNext.apply(_this);
            break;
          // esc
          case 27:
            fClose.apply(_this);
            break;
        }
      });
    },

    /**
     * Disable all key events
     */
    _disable_modal_keyevents: function() {
      $(window).off("keydown");
    },

    /**
     * Helper methods
     */
    _get_prev_or_last: function($from, $all) {
      var prevIndex = $all.index($from) - 1;
      return (prevIndex >= 0) ? $all.eq(prevIndex) : $all.filter(":last");
    },

    _get_next_or_first: function($from, $all) {
      var nextIndex = $all.index($from) + 1;
      return (nextIndex < $all.length) ? $all.eq(nextIndex) : $all.filter(":first");
    },

    _stop_propagation: function(e) {
      e.stopPropagation();
    },

    /**
     * Initialise events
     */
    events: function() {
      var _this = this;

      // Propagation events
      $("body").on("click", $.proxy(this.modals_reset, this));
      this.$wrapperTech.on("click", this._stop_propagation);
      this.$wrapperTimeline.on("click", this._stop_propagation);

      // Technology events
      this.$btnCloseTech.on("click", $.proxy(this.tech_close, this));
      this.$elemsTech.on("click", function() {
        _this.tech_show($(this));
      });

      // Timeline events
      this.$elemsTimeline.on("click", function() {
        _this.timeline_show($(this));
      });
    },
  };

  /**
   * Once the DOM is ready, initialise the experience
   */
  $("document").ready(function() {
    if($("#experience-wrapper").length) {
      experience.init();
    }
  });

})(jQuery);
