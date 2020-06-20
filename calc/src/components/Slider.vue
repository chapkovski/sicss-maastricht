<template>
  <vue-slider
    ref="slider"
    v-model="value"
    :marks="marks"
    :min="parseInt(sliderMin)"
    :max="parseInt(sliderMax)"

    @change="pushval"
  />
</template>

<script>
import VueSlider from "vue-slider-component";
import "vue-slider-component/theme/antd.css";

export default {
  components: {
    VueSlider
  },
  methods: {
    pushval(value, index) {
      this.$emit("change-slider", value);
    }
  },

  props: ["sliderMax", "sliderMin", "sliderInt"],
  data() {
    return {
      value: 0,
       marks: val => val % (this.sliderInt||1) === 0,
    };
  },
  watch: {
    sliderMax() {
      this.$refs.slider.setValue(0);
      this.value =0
    }
  }
};
</script>