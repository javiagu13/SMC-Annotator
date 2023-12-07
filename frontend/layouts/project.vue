<template>
  <v-app>
    <the-header>
      <template #leftDrawerIcon>
        <v-app-bar-nav-icon @click="drawerLeft = !drawerLeft" />
      </template>
    </the-header>

    <v-navigation-drawer v-model="drawerLeft" app clipped color="">
      <the-side-bar :is-project-admin="isProjectAdmin" :project="currentProject" />
    </v-navigation-drawer>

    <v-main>
      <v-container fluid fill-height>
        <v-layout justify-center>
          <v-flex fill-height>
            <SamsungRegex v-if="isProject6" />
            <nuxt />
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex'

import SamsungRegex from '~/pages/SamsungRegex'
import TheHeader from '~/components/layout/TheHeader'
import TheSideBar from '~/components/layout/TheSideBar'


export default {
  components: {
    TheSideBar,
    TheHeader,
    SamsungRegex
  },
  
  data() {
    return {
      drawerLeft: null,
      isProjectAdmin: false,
    }
  },

  computed: {
    ...mapGetters('projects', ['currentProject']),
    isProject6() {
      return /^\/projects\/\d+$/.test(this.$route.path);

    }
  },

mounted() {
    console.log("mounted")
    console.log(this.currentProject._projectType)
  },



  async created() {
    console.log("created:")
    console.log(JSON.stringify(this.currentProject, null, 2));
    console.log(this.currentProject._projectType)
    const member = await this.$repositories.member.fetchMyRole(this.$route.params.id)
    this.isProjectAdmin = member.isProjectAdmin
  }
}


</script>

