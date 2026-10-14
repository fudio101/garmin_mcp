# Changelog

## [0.5.0](https://github.com/fudio101/garmin_mcp/compare/0.4.0...0.5.0) (2026-10-14)


### Features

* **mcpb:** replace the Desktop Extension with an MCP Bundle built on release ([#7](https://github.com/fudio101/garmin_mcp/issues/7)) ([e710ba8](https://github.com/fudio101/garmin_mcp/commit/e710ba8b9c2131510c898979bcb449614b31601a))

## [0.4.0](https://github.com/fudio101/garmin_mcp/compare/0.3.0...0.4.0) (2026-10-13)


### Features

* **mcp:** annotate tool effects for clients ([#411](https://github.com/fudio101/garmin_mcp/issues/411)) ([542cdc2](https://github.com/fudio101/garmin_mcp/commit/542cdc20b271c62dabcc4d88109213332ca93ecd))


### Bug Fixes

* **activities:** null out wrapped-around negative lap distances ([#413](https://github.com/fudio101/garmin_mcp/issues/413)) ([2f05804](https://github.com/fudio101/garmin_mcp/commit/2f05804b3ae9da23b4a9972a40747d3f7c474fe6))
* **analysis:** keep bike power out of running PDC, sign-aware HR drift, timed shift bursts ([#436](https://github.com/fudio101/garmin_mcp/issues/436)) ([5de7248](https://github.com/fudio101/garmin_mcp/commit/5de72486138ce77530c59a77fbf21023ba3bf519))
* **analysis:** use record timestamps instead of assuming 1 record = 1 s ([#437](https://github.com/fudio101/garmin_mcp/issues/437)) ([72b44e2](https://github.com/fudio101/garmin_mcp/commit/72b44e26bcdc87b245d1cf1e6fd1dd380bd3d64b))
* **auth_cli:** don't fail verification for profiles without a full name ([#425](https://github.com/fudio101/garmin_mcp/issues/425)) ([f5c886e](https://github.com/fudio101/garmin_mcp/commit/f5c886e5afef58c94471150773cca663c67810a4))
* **auth:** use the given credentials for password logins and load the profile ([#419](https://github.com/fudio101/garmin_mcp/issues/419)) ([fa16737](https://github.com/fudio101/garmin_mcp/commit/fa167375b35d42418d22a29be9181e9cdf9450eb))
* **challenges:** report the date each personal record was set ([#432](https://github.com/fudio101/garmin_mcp/issues/432)) ([33824bb](https://github.com/fudio101/garmin_mcp/commit/33824bb517a0dd70e8f41a50016273760cf249ef))
* **courses:** real activity typeIds, escaped GPX, safe output path, confirm before delete ([#435](https://github.com/fudio101/garmin_mcp/issues/435)) ([d937eb3](https://github.com/fudio101/garmin_mcp/commit/d937eb36ff241487d1b7b7ab9b1fff1d4c9bc2ee))
* **devices:** summarise the real solar payload in get_device_solar_data ([#424](https://github.com/fudio101/garmin_mcp/issues/424)) ([110dffb](https://github.com/fudio101/garmin_mcp/commit/110dffb0d58f7e45c0d73e5728b810441794e67a))
* **fit:** decode Di2 gear data and L/R power balance per the FIT profile ([#418](https://github.com/fudio101/garmin_mcp/issues/418)) ([b997b6c](https://github.com/fudio101/garmin_mcp/commit/b997b6cbb7f915ee18e951ac0e664d6daf163d3b))
* **gear:** label default activity types by real typeId and list every default ([#431](https://github.com/fudio101/garmin_mcp/issues/431)) ([2367507](https://github.com/fudio101/garmin_mcp/commit/236750793ad8314b4e1b774e11c6fe0b8afb4fd8))
* **health:** fix morning readiness fields, intensity total, and body-comp clustering ([#429](https://github.com/fudio101/garmin_mcp/issues/429)) ([13fabdf](https://github.com/fudio101/garmin_mcp/commit/13fabdf8a2b60b65f36fe455e21468c668a85be1))
* **nutrition:** rename-safe update_custom_food and structured upsert_and_log errors ([#428](https://github.com/fudio101/garmin_mcp/issues/428)) ([aa206ab](https://github.com/fudio101/garmin_mcp/commit/aa206abc3ec4841d85c24f2457744fdacc563ff2))
* **server:** raise a copy of the stored login error on each tool call ([#426](https://github.com/fudio101/garmin_mcp/issues/426)) ([4749f27](https://github.com/fudio101/garmin_mcp/commit/4749f27eda6f09d8483138e65852ff0e2f337061))
* **server:** silence stderr only for the login thread ([#412](https://github.com/fudio101/garmin_mcp/issues/412)) ([08bee29](https://github.com/fudio101/garmin_mcp/commit/08bee2984aeb8dd861b3e066e8a1aa2be85724e9))
* **skills:** babysit-prs CI check and contributor credit ([#438](https://github.com/fudio101/garmin_mcp/issues/438)) ([adfef30](https://github.com/fudio101/garmin_mcp/commit/adfef30b29e26c7271d4cbf9a9101f9796db84a8))
* **training:** lactate-threshold HR history, load-balance device, load-trend wording ([#427](https://github.com/fudio101/garmin_mcp/issues/427)) ([1204897](https://github.com/fudio101/garmin_mcp/commit/1204897f6ef8d914438e5831735577a523ca1e01))
* **weight:** keep caller timestamps and report deletes that did nothing ([#430](https://github.com/fudio101/garmin_mcp/issues/430)) ([327f334](https://github.com/fudio101/garmin_mcp/commit/327f334dd759fd212cadb10d8e8cdc8621a1e46d))
* **workouts:** per-entry schedule_week errors, strict dates, null sportType, full library paging ([#433](https://github.com/fudio101/garmin_mcp/issues/433)) ([968fa19](https://github.com/fudio101/garmin_mcp/commit/968fa192ec4bb63b2e886490fb8e78c6d137a2b3))
* **workouts:** walking sport ID, single recovery HR bound, pace units in docs ([#434](https://github.com/fudio101/garmin_mcp/issues/434)) ([5813ca4](https://github.com/fudio101/garmin_mcp/commit/5813ca4012dd3087cce36cbbd09c5b181ac5c257))
* **write_errors:** report a 5xx after the write was sent as possibly committed ([#423](https://github.com/fudio101/garmin_mcp/issues/423)) ([9258f68](https://github.com/fudio101/garmin_mcp/commit/9258f68c5b7cc373ff364a1934f8327942e41546))

## [0.3.0](https://github.com/fudio101/garmin_mcp/compare/0.2.0...0.3.0) (2026-10-12)


### Features

* **activity:** add delete_activity with a confirmation gate ([68b3547](https://github.com/fudio101/garmin_mcp/commit/68b3547c1e7ce3fac69bb8ad7ed58bdea887d785))
* add a tool to write structured exercise sets to strength activities ([877d43e](https://github.com/fudio101/garmin_mcp/commit/877d43ec9129ef2df88bc2cdded9b18ef0e363f3))
* **http:** add /readyz reporting Garmin login state ([da733f8](https://github.com/fudio101/garmin_mcp/commit/da733f886331577b61d5c823c366ee7f14320c73))
* **http:** add GARMIN_MCP_STATELESS_HTTP to avoid idle session expiry ([48ca02d](https://github.com/fudio101/garmin_mcp/commit/48ca02d3e024ad485ecf90b7229bbd62591ed61f))
* **nutrition:** add brand_name to upsert_and_log ([078d8e3](https://github.com/fudio101/garmin_mcp/commit/078d8e38081d93d55917dde2fa2683190b72a288))
* **nutrition:** return structured errors from food-log write tools ([5e3d379](https://github.com/fudio101/garmin_mcp/commit/5e3d379d4050bebf5f9c69068cd315973552f268))
* **workouts:** add raw option to get_workout_by_id ([f3f4d33](https://github.com/fudio101/garmin_mcp/commit/f3f4d33e1cb26acf5ad969c35594081a06c43ed7))


### Bug Fixes

* **courses:** handle nullable course and geo points ([75bd15e](https://github.com/fudio101/garmin_mcp/commit/75bd15edec34ea94163b8f4c9eb544822fcf0161))
* **dxt:** generate the manifest tools list from registered tools ([7eafdd7](https://github.com/fudio101/garmin_mcp/commit/7eafdd708238d9eab902005aa073a4608959ae12))
* **fit:** read enhanced_altitude/enhanced_speed and record distance ([938d940](https://github.com/fudio101/garmin_mcp/commit/938d940a6567a3ced5dc8093e6a9424a54705773))
* harden Garmin response edge cases ([2f359a7](https://github.com/fudio101/garmin_mcp/commit/2f359a7dfaf34670fb873f0543f3e33f062926d2))
* **nutrition:** preserve serving basis on update_custom_food ([b446dba](https://github.com/fudio101/garmin_mcp/commit/b446dbaa2e39ce4effa680dbc5eaf8e496496f2c))
* **training:** preserve device provenance for training load ([da97721](https://github.com/fudio101/garmin_mcp/commit/da97721cd94545e9afd7e64bb02377f9f9f4de7a))
* **training:** read lactate threshold speed as cm/ms, not inverse pace ([57971ea](https://github.com/fudio101/garmin_mcp/commit/57971ea31c88bf6907bb1515b7dd9fe36bc886aa))
* **workouts:** include adaptive training plan details ([d716630](https://github.com/fudio101/garmin_mcp/commit/d7166301945afa4fffe8e07e9f56fd695a7e526c))
* **workouts:** keep target units and pool length in get_workout_by_id ([a8072b1](https://github.com/fudio101/garmin_mcp/commit/a8072b10ce8d0a113413a18eceee98b5c2b5af2b))
* **workouts:** require confirm=true before deleting workouts ([97df33d](https://github.com/fudio101/garmin_mcp/commit/97df33db42516aa6fb25222f0dcc87f34744cdda))


### Documentation

* document Garmin length limits on free-text tool fields ([cda05d6](https://github.com/fudio101/garmin_mcp/commit/cda05d6f71284ba4998cd5b0d7aabeef6329f81e))
* **nutrition:** correct delete_custom_food's active-reference claim ([3bdab6d](https://github.com/fudio101/garmin_mcp/commit/3bdab6d39b6da8d45de159ddf724b05fe0d74182))
* **workouts:** document custom % FTP power ranges ([8dc6d23](https://github.com/fudio101/garmin_mcp/commit/8dc6d2327b10a7ff07c864ee0b73bfe23ceb8598))

## [0.2.0](https://github.com/fudio101/garmin_mcp/compare/0.1.0...0.2.0) (2026-10-08)


### Features

* **activity:** add generic paginated FIT message endpoint ([c79b442](https://github.com/fudio101/garmin_mcp/commit/c79b442e1622019e190e3b9a11beeb9bc5f376d4))
* add activity write tools for type, notes, effort and feel ([cf1b64b](https://github.com/fudio101/garmin_mcp/commit/cf1b64b4ca4f1ac994cc7e8a93d742a950bfb611))
* add brand_name and trans_fat/calcium/iron/vitamin_d to custom food tools ([ee5e7f4](https://github.com/fudio101/garmin_mcp/commit/ee5e7f49fb82fe1f132210e10932b8b6c4ebf43b))
* add create_run_workout tool for continuous runs ([6334bfa](https://github.com/fudio101/garmin_mcp/commit/6334bfafc08ed5923743724f5638b7867fdfadc6))
* add create_run_workout tool for continuous runs ([037496a](https://github.com/fudio101/garmin_mcp/commit/037496a882babd78b228570aa89c1aef04c66f17))
* add create_run_workout tool for continuous runs ([7be6899](https://github.com/fudio101/garmin_mcp/commit/7be68993c708c9c904516e4edf4d2f563bbca430))
* add cycling VO2 max to training status ([1e0824a](https://github.com/fudio101/garmin_mcp/commit/1e0824a11fe7bab46d36edfd2c79cf69f870b5a8))
* add cycling VO2 max to training status ([9e442c2](https://github.com/fudio101/garmin_mcp/commit/9e442c238ee32c78cac00e3432b1d40c48823732))
* add delete_custom_food tool ([a0c49d4](https://github.com/fudio101/garmin_mcp/commit/a0c49d4e66923c633f52b2464e2445c718c15497))
* add event_type field and pagination to activity listing tools ([4b158d4](https://github.com/fudio101/garmin_mcp/commit/4b158d414aa440350c0b5fb2e6ba769bd9126771))
* add eventType to activity summary responses ([a2663ea](https://github.com/fudio101/garmin_mcp/commit/a2663ea85819bb140a077c233a6081e1a1e82140))
* add opencode project config for local Garmin MCP ([7af73eb](https://github.com/fudio101/garmin_mcp/commit/7af73ebf9b4073cf3b1ad1cb42d351f38e7ef47c))
* add pagination to get_activities_by_date ([abf2ae3](https://github.com/fudio101/garmin_mcp/commit/abf2ae36d668d02314e63e8b9d332caf02bb45af))
* add per-sport heart rate zone reads and writes ([fdb5a9e](https://github.com/fudio101/garmin_mcp/commit/fdb5a9eba494f5f3657c65b91e36925c14d6a6b9)), closes [#276](https://github.com/fudio101/garmin_mcp/issues/276)
* add set_nutrition_daily_settings tool to update calorie and macro goals (closes [#181](https://github.com/fudio101/garmin_mcp/issues/181)) ([#206](https://github.com/fudio101/garmin_mcp/issues/206)) ([68ca159](https://github.com/fudio101/garmin_mcp/commit/68ca159cb40f2dbba551add8bf27515bc33bdb4b))
* add tools to download activity files (.fit/.gpx/.tcx/.csv) to disk ([d31de79](https://github.com/fudio101/garmin_mcp/commit/d31de7980d652289e5368637261fcd17aa2c7d90))
* add unschedule_workout and unschedule_workouts tools ([54d1291](https://github.com/fudio101/garmin_mcp/commit/54d1291f46aabff6081686071fce727f5202acdf))
* apply PRs [#140](https://github.com/fudio101/garmin_mcp/issues/140)/[#141](https://github.com/fudio101/garmin_mcp/issues/141)/[#142](https://github.com/fudio101/garmin_mcp/issues/142) and implement Issues [#137](https://github.com/fudio101/garmin_mcp/issues/137)/[#138](https://github.com/fudio101/garmin_mcp/issues/138)/[#139](https://github.com/fudio101/garmin_mcp/issues/139) ([004e762](https://github.com/fudio101/garmin_mcp/commit/004e762188756a6953a7dd4d2105b95a2a82e1e8))
* **calendar:** add goal_time_seconds and fix distance_meters units ([9e29926](https://github.com/fudio101/garmin_mcp/commit/9e2992642b01a9ca07036bd30e3ebc80b5ad4d52))
* **calendar:** expose races and events from the Garmin calendar ([504e6c4](https://github.com/fudio101/garmin_mcp/commit/504e6c47fd4386005875d6a9d545aa33c205b1fc)), closes [#258](https://github.com/fudio101/garmin_mcp/issues/258)
* complete custom-food lifecycle (rebase of [#152](https://github.com/fudio101/garmin_mcp/issues/152)) ([c7d140a](https://github.com/fudio101/garmin_mcp/commit/c7d140a0839fda34701c869f866a34046154859a))
* **courses:** add get_course_details and download_course_gpx tools ([3c44049](https://github.com/fudio101/garmin_mcp/commit/3c440499a3082a93344530a20d741b06010ad1e1))
* **health:** add get_energy_balance to derive measured TDEE ([38e88c3](https://github.com/fudio101/garmin_mcp/commit/38e88c311a39fcb2066856138e006f197c30b923))
* **health:** add get_sleep_summary_range for multi-night sleep queries ([572fc70](https://github.com/fudio101/garmin_mcp/commit/572fc70f76f4f7dc4e023777cfc73aee904210c8))
* **health:** add get_stats_range for multi-day calorie/step totals ([e2cf67c](https://github.com/fudio101/garmin_mcp/commit/e2cf67c1b6ac7529c2ccd141ace02c55103ef77a))
* **health:** expose daily recovery time remaining ([f4fc10b](https://github.com/fudio101/garmin_mcp/commit/f4fc10bd61499b1986cc4242f059aa0de4b1baee))
* **nutrition:** add get_nutrition_summary_between_dates for multi-day intake totals ([86adde9](https://github.com/fudio101/garmin_mcp/commit/86adde9b12cf2c150941d9d1c5537df269cbb5ce))
* **nutrition:** add search_foods catalog tool + source routing for log_custom_food (closes [#164](https://github.com/fudio101/garmin_mcp/issues/164)) ([#225](https://github.com/fudio101/garmin_mcp/issues/225)) ([a16f057](https://github.com/fudio101/garmin_mcp/commit/a16f05770291fd25e35c58db17f9e77e70facbc2))
* publish versioned multi-arch Docker images to GHCR ([7003765](https://github.com/fudio101/garmin_mcp/commit/7003765fae85a675851881eca94a043507ba45b9)), closes [#136](https://github.com/fudio101/garmin_mcp/issues/136) [#337](https://github.com/fudio101/garmin_mcp/issues/337)
* serve MCP over HTTP (streamable-http/sse) transports ([66a70fc](https://github.com/fudio101/garmin_mcp/commit/66a70fc9433164f374c915299e5fc041765c8062))
* support custom bpm heart-rate range in create_run_workout ([#224](https://github.com/fudio101/garmin_mcp/issues/224)) ([d38dd64](https://github.com/fudio101/garmin_mcp/commit/d38dd64a66ec52cd043dfe0c675eae7bdd663dc8))
* **training:** add get_acclimation for heat and altitude acclimation status ([e8554bc](https://github.com/fudio101/garmin_mcp/commit/e8554bcd761a4494dc12a98461224bb3dcf1fbc5))
* **training:** add Running Tolerance tools ([d6c9b40](https://github.com/fudio101/garmin_mcp/commit/d6c9b40540659531a282a33db554da32d848fe3e)), closes [#239](https://github.com/fudio101/garmin_mcp/issues/239)
* **training:** fall back to profile VO2 max when trend history is unavailable ([#240](https://github.com/fudio101/garmin_mcp/issues/240)) ([3619b9a](https://github.com/fudio101/garmin_mcp/commit/3619b9a12670e039d8abb6c7a3c7e30b2c14ff44))
* **workout:** add create_run_interval_workout for repeat-based interval runs ([6fe000e](https://github.com/fudio101/garmin_mcp/commit/6fe000e18cefcbbf7761d16495a0f8fda7aff764))
* **workouts:** expose Garmin Coach workouts (closes [#231](https://github.com/fudio101/garmin_mcp/issues/231)) ([#243](https://github.com/fudio101/garmin_mcp/issues/243)) ([3610be6](https://github.com/fudio101/garmin_mcp/commit/3610be6feed93088d85b0f35aba9d7d07c2505a7))


### Bug Fixes

* **auth:** fail when saved tokens don't authenticate ([3dd6b3c](https://github.com/fudio101/garmin_mcp/commit/3dd6b3ccba05e5c56d4198f25aef398dd9673d37))
* bound Garmin call duration so a stalled request can't hang the server ([#248](https://github.com/fudio101/garmin_mcp/issues/248)) ([#254](https://github.com/fudio101/garmin_mcp/issues/254)) ([13ca0ed](https://github.com/fudio101/garmin_mcp/commit/13ca0ed3f1c0c437deec58624eaf831a1b36a25d))
* cap mcp &lt;2 so fresh installs stop resolving to the 2.x API (closes [#226](https://github.com/fudio101/garmin_mcp/issues/226)) ([#227](https://github.com/fudio101/garmin_mcp/issues/227)) ([d3056af](https://github.com/fudio101/garmin_mcp/commit/d3056afb63d38950addf3133bace3044f242bdac))
* **challenges:** return Connect UI goals from get_goals ([c99194b](https://github.com/fudio101/garmin_mcp/commit/c99194b2aa95579d0e233be40863e5463a2e0d08))
* change server.type from 'uv' to 'python' in DXT manifest (closes [#188](https://github.com/fudio101/garmin_mcp/issues/188)) ([#203](https://github.com/fudio101/garmin_mcp/issues/203)) ([50e3a42](https://github.com/fudio101/garmin_mcp/commit/50e3a42f6695409fb09ba38b9145695909e13b85))
* correct run_seconds display units and add create_run_workout integration tests ([315ab9d](https://github.com/fudio101/garmin_mcp/commit/315ab9d2c61b345021271cafbb91d980805e721e))
* delete_food_log now correctly removes QUICK_ADD and REGULAR_LOG entries ([db82d35](https://github.com/fudio101/garmin_mcp/commit/db82d35d2d823abfef18c5e08ee1a7db1c70b9fa))
* delete_workout dict.status_code, large activity IDs, schedule idempotency ([f9a0619](https://github.com/fudio101/garmin_mcp/commit/f9a0619b770a33298d60de1d2e247203429320ca))
* delete_workout dict.status_code, large activity IDs, schedule idempotency ([6320152](https://github.com/fudio101/garmin_mcp/commit/6320152a81be6ee5d3fc00ade7782536aa5b3a7c))
* **dxt:** resolve token path ${HOME} and handle unset optional user_config (closes [#204](https://github.com/fudio101/garmin_mcp/issues/204)) ([#220](https://github.com/fudio101/garmin_mcp/issues/220)) ([ff0bed5](https://github.com/fudio101/garmin_mcp/commit/ff0bed5463da731ac541c678a2015a992ee23073))
* harden null-section handling in HRV, sleep, progress, body-battery, and scheduled-workout tools ([#253](https://github.com/fudio101/garmin_mcp/issues/253)) ([5977799](https://github.com/fudio101/garmin_mcp/commit/597779998df7f938078b438f0ee05b6646f52388))
* **health:** don't crash on a night with null sleep-phase breakdowns ([ead25df](https://github.com/fudio101/garmin_mcp/commit/ead25dfc9898fe40d0caa82a27f9add932c575b5))
* improve Garmin tool defaults and calendar chunking ([5dd2a1a](https://github.com/fudio101/garmin_mcp/commit/5dd2a1a9df044113651b42cbdd07a108089537e0))
* improve Garmin tool defaults and calendar chunking ([54955ec](https://github.com/fudio101/garmin_mcp/commit/54955ec865d9b7d245e06f997d915ea5f0c77b2f))
* keep the original error message when translating Garmin exceptions ([6c84f7c](https://github.com/fudio101/garmin_mcp/commit/6c84f7ccf7ab496621357bb4e5e603ee4018fa13)), closes [#299](https://github.com/fudio101/garmin_mcp/issues/299)
* map virtual challenge fields (closes [#212](https://github.com/fudio101/garmin_mcp/issues/212)) ([#219](https://github.com/fudio101/garmin_mcp/issues/219)) ([f80702d](https://github.com/fudio101/garmin_mcp/commit/f80702ddf9db1ee5e3f0c477ae13138145b78a68))
* **mcp:** disable auto structured_output for string tools ([8163e3a](https://github.com/fudio101/garmin_mcp/commit/8163e3ab18d01d3087bb5ef7197de2f721dc82d5))
* move nested workout target bounds to step level (closes [#210](https://github.com/fudio101/garmin_mcp/issues/210)) ([#221](https://github.com/fudio101/garmin_mcp/issues/221)) ([b6b739d](https://github.com/fudio101/garmin_mcp/commit/b6b739d21c252905191d78b2dc9eaa3a03bc7ba1))
* nutrition write tools crash on success; delete_food_log rejects UUID log IDs ([300b9ee](https://github.com/fudio101/garmin_mcp/commit/300b9eed9d8e38fbab5124dbd0d501bc50f57330))
* nutrition write tools crash on success; delete_food_log uses correct endpoint ([2f9e34e](https://github.com/fudio101/garmin_mcp/commit/2f9e34ea49db18d9b2d16a86a53019b631f61987))
* **nutrition:** explain the weight-goal targetDate that blocks every settings update ([cfc5d79](https://github.com/fudio101/garmin_mcp/commit/cfc5d799ab0f165e837f1188a1d093c65838aaf7))
* **nutrition:** separate query parameters from URL paths ([ce3f903](https://github.com/fudio101/garmin_mcp/commit/ce3f903ac9095cd47ac6780236e7b39cfdc373e8))
* **nutrition:** use calorieGoal and nested macroGoals settings ([aa2eab1](https://github.com/fudio101/garmin_mcp/commit/aa2eab169497a83091fe937b3589e735dba183d0))
* power.between must use workoutTargetTypeId 6 not 2 for cycling (Issue [#155](https://github.com/fudio101/garmin_mcp/issues/155)). Co-Authored-By: Claude Sonnet 4.6 &lt;noreply@anthropic.com&gt; ([12833d4](https://github.com/fudio101/garmin_mcp/commit/12833d431d6c89e60b14be3586a4fbbd94bba14e))
* power.between target type for cycling workouts (Issue [#155](https://github.com/fudio101/garmin_mcp/issues/155)) ([2974244](https://github.com/fudio101/garmin_mcp/commit/2974244bfda1595b00836b3f942f579ec2d6f7d6))
* remove unused resp assignment in delete_custom_food ([b70209c](https://github.com/fudio101/garmin_mcp/commit/b70209c42781164222fe797bdaa208132ca832d0))
* replace garth references in courses.py with garminconnect 0.3.x client API ([9dfb1be](https://github.com/fudio101/garmin_mcp/commit/9dfb1bec5559fb8306f8de44ad30b4fcb6731377))
* replace garth references in courses.py with garminconnect 0.3.x client API ([a7af065](https://github.com/fudio101/garmin_mcp/commit/a7af0658ad7c950e2991667b893264d5fd507991)), closes [#107](https://github.com/fudio101/garmin_mcp/issues/107)
* run seconds to minutes in description, add create_run_workout integration tests ([b0f3e53](https://github.com/fudio101/garmin_mcp/commit/b0f3e5336e3ace1f74995ba4168faa718202fc1e))
* sanitize RepeatGroupDTO endCondition before upload to prevent API corruption ([f625d66](https://github.com/fudio101/garmin_mcp/commit/f625d66ec86ed1d27fab75d6e6b2238ec4d09781))
* sanitize RepeatGroupDTO endCondition before upload to prevent API corruption ([cf8da67](https://github.com/fudio101/garmin_mcp/commit/cf8da6744829ea72e79a40399d91a4efa209a554)), closes [#112](https://github.com/fudio101/garmin_mcp/issues/112)
* schedule_week stale garth.post + apply idempotency ([b55c2e0](https://github.com/fudio101/garmin_mcp/commit/b55c2e0eb47fccdf9ce37589ecf0e2e8d1af46d3))
* **server:** reject nonblank empty tool allowlists ([0ed705f](https://github.com/fudio101/garmin_mcp/commit/0ed705f5d55e164c03ad63d0d6b7e4b5cd3300cb))
* **server:** start Garmin login in the background instead of blocking the MCP handshake ([35d5b29](https://github.com/fudio101/garmin_mcp/commit/35d5b293d404f4f6c49174de89ecc9650b2e02dc))
* suppress stdout during garminconnect login to prevent MCP stdio corruption (closes [#166](https://github.com/fudio101/garmin_mcp/issues/166)) ([#205](https://github.com/fudio101/garmin_mcp/issues/205)) ([e79564b](https://github.com/fudio101/garmin_mcp/commit/e79564b1f464034dcc3d0fd0b1b3db68a30af654))
* surface description and event type in get_activity ([ff75384](https://github.com/fudio101/garmin_mcp/commit/ff7538488300b26dc768c8562420fe40c7acf65d))
* **tests:** correct _running_workout_with_steps call signature in secondary target type test ([#135](https://github.com/fudio101/garmin_mcp/issues/135)) ([50e88c1](https://github.com/fudio101/garmin_mcp/commit/50e88c1e872d598a2b2d9135691050e169e93c74))
* token permissions, runtime error proxy, create_manual_activity, and transport config improvements ([26b31e3](https://github.com/fudio101/garmin_mcp/commit/26b31e377a4c6aa625a70ad9b5e97fecb5e808b7))
* **training:** carry VO2 max values forward so trend matches the Connect chart ([56e8ca2](https://github.com/fudio101/garmin_mcp/commit/56e8ca2eae40b1c1425cce656da3ebd4e62410cf))
* **training:** correct calories units and drop misleading fields in progress summary ([2b1e4d2](https://github.com/fudio101/garmin_mcp/commit/2b1e4d20744fd813be02f48e71792be060983cd4))
* **training:** correct lactate threshold speed unit conversion ([65f0cbd](https://github.com/fudio101/garmin_mcp/commit/65f0cbd3c12c0741919c8984cf17573303e782eb))
* **training:** fall back to activity list when training effect details 403 ([d8d0a5d](https://github.com/fudio101/garmin_mcp/commit/d8d0a5d356072c61b23c75f11a799ac3345c77c8))
* **training:** populate nightly HRV and period averages ([f00569f](https://github.com/fudio101/garmin_mcp/commit/f00569f27e416547c5a7bbf08fbb4b9e4a939ee2))
* **training:** tolerate null device map entries in get_training_status ([fa1ec72](https://github.com/fudio101/garmin_mcp/commit/fa1ec72a0ad64b657fdb91bd0ecf9ecd412425da))
* upsert_and_log dedup (Bug A) and update_custom_food merge (Bug B) ([e6dca70](https://github.com/fudio101/garmin_mcp/commit/e6dca703690d002b62bdffe6f740a6e2a5b75353))
* validate date inputs and gpx path to prevent injection and file read ([0a532cd](https://github.com/fudio101/garmin_mcp/commit/0a532cdd3be7330d53b0714282ede87821370d9e))
* validate workout end condition mappings to prevent silent data corruption ([f56d94a](https://github.com/fudio101/garmin_mcp/commit/f56d94a0b9d14be0db65c4ff571f25dbf6a59151))
* validate workout target type mappings to prevent silent data corruption ([5f10cc0](https://github.com/fudio101/garmin_mcp/commit/5f10cc0864762f3dac4f5b1f0337cd5d6757dc13))
* **weather:** correct temperature unit + label wind for activity weather ([#223](https://github.com/fudio101/garmin_mcp/issues/223)) ([0195fa0](https://github.com/fudio101/garmin_mcp/commit/0195fa0bdad89b2b9011d227494f51cb38617f43))
* **weather:** temperature_celsius label was wrong for imperial accounts ([#163](https://github.com/fudio101/garmin_mcp/issues/163)) ([cc3d853](https://github.com/fudio101/garmin_mcp/commit/cc3d85350d0a28eb4665e222bf342a5e68c1bdc6))
* **windows:** force LF line endings on stdout for stdio transport ([29ef00e](https://github.com/fudio101/garmin_mcp/commit/29ef00e499810096b6ab693bbb87893ad5b28d1d))
* **windows:** force LF line endings on stdout for stdio transport ([4a36c19](https://github.com/fudio101/garmin_mcp/commit/4a36c19d744a18e668c70173f59d7ec79d2b7805))
* **workouts:** compare exercises by index, not value, for rest-step skip ([b400067](https://github.com/fudio101/garmin_mcp/commit/b400067ba6ae2571898982493d1b238cf86e0d11))
* **workouts:** emit repeat groups so multi-set strength exercises keep their set count ([b8ea726](https://github.com/fudio101/garmin_mcp/commit/b8ea726564b6db4b4844306d0efad1bb28541564))
* **workouts:** stop sending an invalid category on strength steps ([#222](https://github.com/fudio101/garmin_mcp/issues/222)) ([2819c4c](https://github.com/fudio101/garmin_mcp/commit/2819c4ccc237836cc131ca8fcb1bfce3858e9e84))


### Documentation

* **activity:** remove false event_type 'pre-dates API' docstring claim ([#165](https://github.com/fudio101/garmin_mcp/issues/165)) ([3ee7c97](https://github.com/fudio101/garmin_mcp/commit/3ee7c978607513b5687dd528d61b42ab1e23b93d))
* Add Codex MCP setup instructions ([b05ec9a](https://github.com/fudio101/garmin_mcp/commit/b05ec9ae106f2e126e1848d1f02fa5bdbafc9553))
* Add Codex MCP setup instructions ([d6f8064](https://github.com/fudio101/garmin_mcp/commit/d6f8064d2dac7a25f7242904ce94ba36d064cff2))
* document endConditionZone for zone-based HR end conditions ([0c59dd2](https://github.com/fudio101/garmin_mcp/commit/0c59dd2791a932693e9371306412c43bca8da1fe))
* document running multiple Garmin accounts via GARMINTOKENS ([655efb8](https://github.com/fudio101/garmin_mcp/commit/655efb8f5639602f661c26164282d0ddd4f5d3db))
* document the prebuilt image and the release workflow ([d5d184c](https://github.com/fudio101/garmin_mcp/commit/d5d184c7f7b46e3d3c669c0b72798e6c31c21d14))
* troubleshoot Windows Smart App Control blocking uv/uvx ([8ddcc9b](https://github.com/fudio101/garmin_mcp/commit/8ddcc9b4de9d1dc9087153e1d8a50a09cf68d83e))
* update tool docstrings with production-verified field behavior ([f840650](https://github.com/fudio101/garmin_mcp/commit/f8406500d316a26ec02615b4b3c07eaffce5fc7a))
