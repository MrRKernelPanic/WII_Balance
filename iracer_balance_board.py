




<!DOCTYPE html>
<html class="   ">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    
    
    <title>iracer-controllers/iracer_balance_board/iracer_balance_board.py at master · conoro/iracer-controllers · GitHub</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="conoro/iracer-controllers" name="twitter:title" /><meta content="iracer-controllers - Control Arexx Dagu i-racer using a variety of inputs such as  MaKey MaKey + Raspberry Pi + Bluetooth" name="twitter:description" /><meta content="https://avatars1.githubusercontent.com/u/586566?s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars1.githubusercontent.com/u/586566?s=400" property="og:image" /><meta content="conoro/iracer-controllers" property="og:title" /><meta content="https://github.com/conoro/iracer-controllers" property="og:url" /><meta content="iracer-controllers - Control Arexx Dagu i-racer using a variety of inputs such as  MaKey MaKey + Raspberry Pi + Bluetooth" property="og:description" />

    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    

    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="5E48DC67:6286:A34AC:539B93EA" name="octolytics-dimension-request_id" />
    

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico" />


    <meta content="authenticity_token" name="csrf-param" />
<meta content="X/VxNQaJezUvnzd7v3vMfx2/WjBe0+GCATv2HutVE1mRgWmX5Pmy62vj8G1G9D3bozw2fZDR4LQmtVZoM/r5ow==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-947f3b2fd0b84c13ecc4244435f75bfed024bbe1.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://assets-cdn.github.com/assets/github2-86c2efc9edae70ed18c76b856d22e0b7eead05f1.css" media="all" rel="stylesheet" type="text/css" />
    


    <meta http-equiv="x-pjax-version" content="a14101df690a9b7064272350e321873d">

      
  <meta name="description" content="iracer-controllers - Control Arexx Dagu i-racer using a variety of inputs such as  MaKey MaKey + Raspberry Pi + Bluetooth" />

  <meta content="586566" name="octolytics-dimension-user_id" /><meta content="conoro" name="octolytics-dimension-user_login" /><meta content="7427230" name="octolytics-dimension-repository_id" /><meta content="conoro/iracer-controllers" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="7427230" name="octolytics-dimension-repository_network_root_id" /><meta content="conoro/iracer-controllers" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/conoro/iracer-controllers/commits/master.atom" rel="alternate" title="Recent Commits to iracer-controllers:master" type="application/atom+xml" />

  </head>


  <body class="logged_out  env-production  vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      
      <div class="header header-logged-out">
  <div class="container clearfix">

    <a class="header-logo-wordmark" href="https://github.com/">
      <span class="mega-octicon octicon-logo-github"></span>
    </a>

    <div class="header-actions">
        <a class="button primary" href="/join">Sign up</a>
      <a class="button signin" href="/login?return_to=%2Fconoro%2Firacer-controllers%2Fblob%2Fmaster%2Firacer_balance_board%2Firacer_balance_board.py">Sign in</a>
    </div>

    <div class="command-bar js-command-bar  in-repository">

      <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
        <li class="features"><a href="/features">Features</a></li>
          <li class="enterprise"><a href="https://enterprise.github.com/">Enterprise</a></li>
          <li class="blog"><a href="/blog">Blog</a></li>
      </ul>
        <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<div class="commandbar">
  <span class="message"></span>
  <input type="text" data-hotkey="s, /" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    
      data-repo="conoro/iracer-controllers"
      data-branch="master"
      data-sha="e00cfad55a15d3e330c8b0ca5195495c1f27f4d5"
  >
  <div class="display hidden"></div>
</div>

    <input type="hidden" name="nwo" value="conoro/iracer-controllers" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
    </div>

  </div>
</div>



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">


  <li>
    <a href="/login?return_to=%2Fconoro%2Firacer-controllers"
    class="minibutton with-count star-button tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <span class="octicon octicon-star"></span>Star
  </a>

    <a class="social-count js-social-count" href="/conoro/iracer-controllers/stargazers">
      6
    </a>

  </li>

    <li>
      <a href="/login?return_to=%2Fconoro%2Firacer-controllers"
        class="minibutton with-count js-toggler-target fork-button tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <span class="octicon octicon-repo-forked"></span>Fork
      </a>
      <a href="/conoro/iracer-controllers/network" class="social-count">
        4
      </a>
    </li>
</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/conoro" class="url fn" itemprop="url" rel="author"><span itemprop="title">conoro</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/conoro/iracer-controllers" class="js-current-repository js-repo-home-link">iracer-controllers</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/conoro/iracer-controllers" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /conoro/iracer-controllers">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/conoro/iracer-controllers/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g i" data-selected-links="repo_issues /conoro/iracer-controllers/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>0</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/conoro/iracer-controllers/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-hotkey="g p" data-selected-links="repo_pulls /conoro/iracer-controllers/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/conoro/iracer-controllers/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /conoro/iracer-controllers/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/conoro/iracer-controllers/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /conoro/iracer-controllers/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Network">
        <a href="/conoro/iracer-controllers/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /conoro/iracer-controllers/network">
          <span class="octicon octicon-repo-forked"></span> <span class="full-word">Network</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/conoro/iracer-controllers.git" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/conoro/iracer-controllers.git" data-copied-hint="copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/conoro/iracer-controllers" readonly="readonly">
    <span class="url-box-clippy">
    <button aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="https://github.com/conoro/iracer-controllers" data-copied-hint="copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>



                <a href="/conoro/iracer-controllers/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download conoro/iracer-controllers as a zip file"
                   title="Download conoro/iracer-controllers as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<a href="/conoro/iracer-controllers/blob/c714032e27f947fde9bd8e91850461a4ebcd5076/iracer_balance_board/iracer_balance_board.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:c7ad6a4e35098acc8d84ca541df9df47 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/conoro/iracer-controllers/blob/master/iracer_balance_board/iracer_balance_board.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="button-group right">
    <a href="/conoro/iracer-controllers/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button class="js-zeroclipboard minibutton zeroclipboard-button"
          data-clipboard-text="iracer_balance_board/iracer_balance_board.py"
          aria-label="Copy to clipboard"
          data-copied-hint="Copied!">
      <span class="octicon octicon-clippy"></span>
    </button>
  </div>

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/conoro/iracer-controllers" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">iracer-controllers</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/conoro/iracer-controllers/tree/master/iracer_balance_board" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">iracer_balance_board</span></a></span><span class="separator"> / </span><strong class="final-path">iracer_balance_board.py</strong>
  </div>
</div>


  <div class="commit file-history-tease">
      <img alt="Conor O&#39;Neill" class="main-avatar js-avatar" data-user="586566" height="24" src="https://avatars2.githubusercontent.com/u/586566?s=140" width="24" />
      <span class="author"><a href="/conoro" rel="author">conoro</a></span>
      <time datetime="2013-05-06T16:46:30+01:00" is="relative-time">May 06, 2013</time>
      <div class="commit-title">
          <a href="/conoro/iracer-controllers/commit/eeac61e39e1722ed387db0eae6804e350c876f3f" class="message" data-pjax="true" title="added code for Wii Balance Board + Raspberry Pi">added code for Wii Balance Board + Raspberry Pi</a>
      </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong>  contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="Conor O&#39;Neill" class=" js-avatar" data-user="586566" height="24" src="https://avatars2.githubusercontent.com/u/586566?s=140" width="24" />
            <a href="/conoro">conoro</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
        <span class="meta-divider"></span>
          <span>157 lines (126 sloc)</span>
          <span class="meta-divider"></span>
        <span>6.51 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
              <a class="minibutton disabled tooltipped tooltipped-w" href="#"
                 aria-label="You must be signed in to make or propose changes">Edit</a>
          <a href="/conoro/iracer-controllers/raw/master/iracer_balance_board/iracer_balance_board.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/conoro/iracer-controllers/blame/master/iracer_balance_board/iracer_balance_board.py" class="button minibutton js-update-url-with-hash">Blame</a>
          <a href="/conoro/iracer-controllers/commits/master/iracer_balance_board/iracer_balance_board.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger disabled empty-icon tooltipped tooltipped-w" href="#"
             aria-label="You must be signed in to make or propose changes">
          Delete
        </a>
      </div><!-- /.actions -->
    </div>
      
  <div class="blob-wrapper data type-python js-blob-data">
       <table class="file-code file-diff tab-size-8">
         <tr class="file-code-line">
           <td class="blob-line-nums">
             <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>

           </td>
           <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="c">#!/usr/bin/env python</span></div><div class='line' id='LC2'><span class="c"># -*- coding: utf-8 -*-</span></div><div class='line' id='LC3'><span class="c">#</span></div><div class='line' id='LC4'><span class="c"># Copyright (C) 2013 Conor O&#39;Neill</span></div><div class='line' id='LC5'><span class="c">#</span></div><div class='line' id='LC6'><span class="c"># Licensed under the Apache License, Version 2.0 (the &quot;License&quot;);</span></div><div class='line' id='LC7'><span class="c"># you may not use this file except in compliance with the License.</span></div><div class='line' id='LC8'><span class="c"># You may obtain a copy of the License at</span></div><div class='line' id='LC9'><span class="c">#</span></div><div class='line' id='LC10'><span class="c">#      http://www.apache.org/licenses/LICENSE-2.0</span></div><div class='line' id='LC11'><span class="c">#</span></div><div class='line' id='LC12'><span class="c"># Unless required by applicable law or agreed to in writing, software</span></div><div class='line' id='LC13'><span class="c"># distributed under the License is distributed on an &quot;AS IS&quot; BASIS,</span></div><div class='line' id='LC14'><span class="c"># WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.</span></div><div class='line' id='LC15'><span class="c"># See the License for the specific language governing permissions and</span></div><div class='line' id='LC16'><span class="c"># limitations under the License.</span></div><div class='line' id='LC17'><br/></div><div class='line' id='LC18'><span class="sd">&quot;&quot;&quot;Simple code to control Arexx Dagu i-racer using Raspberry Pi and Wii Balance Board</span></div><div class='line' id='LC19'><br/></div><div class='line' id='LC20'><span class="sd">Usage:</span></div><div class='line' id='LC21'><span class="sd">  $ python iracer_balance_board.py</span></div><div class='line' id='LC22'><br/></div><div class='line' id='LC23'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC24'><br/></div><div class='line' id='LC25'><span class="n">__author__</span> <span class="o">=</span> <span class="s">&#39;cwjoneill@gmail.com (Conor O</span><span class="se">\&#39;</span><span class="s">Neill)&#39;</span></div><div class='line' id='LC26'><br/></div><div class='line' id='LC27'><span class="kn">import</span> <span class="nn">cwiid</span></div><div class='line' id='LC28'><span class="kn">import</span> <span class="nn">sys</span></div><div class='line' id='LC29'><span class="kn">import</span> <span class="nn">bluetooth</span></div><div class='line' id='LC30'><span class="kn">import</span> <span class="nn">time</span></div><div class='line' id='LC31'><span class="kn">import</span> <span class="nn">math</span></div><div class='line' id='LC32'><br/></div><div class='line' id='LC33'><span class="k">global</span> <span class="n">sock</span></div><div class='line' id='LC34'><span class="k">global</span> <span class="n">wiimote</span></div><div class='line' id='LC35'>&nbsp;</div><div class='line' id='LC36'><span class="k">def</span> <span class="nf">main</span><span class="p">():</span></div><div class='line' id='LC37'><br/></div><div class='line' id='LC38'><br/></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="s">&#39;Press Red Sync Button in Battery Compartment of Balance Board...&#39;</span></div><div class='line' id='LC40'><br/></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Wii Balance Board</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rpt_mode</span> <span class="o">=</span> <span class="mi">0</span></div><div class='line' id='LC43'><br/></div><div class='line' id='LC44'>	<span class="c"># Change the number below to the Bluetooth MAC address of your Wii Balance Board</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># You get that by pressing red sync button in battery compartment and then running</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># hcitool scan	</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">wiimote</span> <span class="o">=</span> <span class="n">cwiid</span><span class="o">.</span><span class="n">Wiimote</span><span class="p">(</span><span class="s">&quot;00:1E:35:C0:E3:FD&quot;</span><span class="p">)</span></div><div class='line' id='LC48'><br/></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">rpt_mode</span> <span class="o">^=</span> <span class="n">cwiid</span><span class="o">.</span><span class="n">RPT_EXT</span></div><div class='line' id='LC50'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">wiimote</span><span class="o">.</span><span class="n">rpt_mode</span> <span class="o">=</span> <span class="n">rpt_mode</span></div><div class='line' id='LC51'><br/></div><div class='line' id='LC52'><br/></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># i-racer </span></div><div class='line' id='LC54'>	<span class="c"># Change the number below to the Bluetooth MAC address of your i-racer</span></div><div class='line' id='LC55'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># You get that by turning on the i-racer and and then running</span></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># hcitool scan	</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">bd_addr</span> <span class="o">=</span> <span class="s">&quot;00:12:05:09:95:33&quot;</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">port</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sock</span> <span class="o">=</span> <span class="n">bluetooth</span><span class="o">.</span><span class="n">BluetoothSocket</span><span class="p">(</span> <span class="n">bluetooth</span><span class="o">.</span><span class="n">RFCOMM</span> <span class="p">)</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sock</span><span class="o">.</span><span class="n">connect</span><span class="p">((</span><span class="n">bd_addr</span><span class="p">,</span> <span class="n">port</span><span class="p">))</span></div><div class='line' id='LC61'><br/></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Probably a good idea to have recently calibrated your Balance Board on your Wii</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">balance_calibration</span> <span class="o">=</span> <span class="n">wiimote</span><span class="o">.</span><span class="n">get_balance_cal</span><span class="p">()</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># print balance_calibration</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">right_top_cal</span> <span class="o">=</span> <span class="n">balance_calibration</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">right_bottom_cal</span> <span class="o">=</span> <span class="n">balance_calibration</span><span class="p">[</span><span class="mi">1</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">left_top_cal</span> <span class="o">=</span> <span class="n">balance_calibration</span><span class="p">[</span><span class="mi">2</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">left_bottom_cal</span> <span class="o">=</span> <span class="n">balance_calibration</span><span class="p">[</span><span class="mi">3</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC69'><br/></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">while</span> <span class="bp">True</span><span class="p">:</span></div><div class='line' id='LC71'>	    <span class="c"># Quite a slow refresh rate. Feel free to reduce this time (it&#39;s in seconds)</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mf">0.5</span><span class="p">)</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">wiimote</span><span class="o">.</span><span class="n">request_status</span><span class="p">()</span></div><div class='line' id='LC74'><br/></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">right_top</span> <span class="o">=</span> <span class="n">wiimote</span><span class="o">.</span><span class="n">state</span><span class="p">[</span><span class="s">&#39;balance&#39;</span><span class="p">][</span><span class="s">&#39;right_top&#39;</span><span class="p">]</span> <span class="o">-</span> <span class="n">right_top_cal</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">right_bottom</span> <span class="o">=</span>  <span class="n">wiimote</span><span class="o">.</span><span class="n">state</span><span class="p">[</span><span class="s">&#39;balance&#39;</span><span class="p">][</span><span class="s">&#39;right_bottom&#39;</span><span class="p">]</span> <span class="o">-</span> <span class="n">right_bottom_cal</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">left_top</span> <span class="o">=</span>  <span class="n">wiimote</span><span class="o">.</span><span class="n">state</span><span class="p">[</span><span class="s">&#39;balance&#39;</span><span class="p">][</span><span class="s">&#39;left_top&#39;</span><span class="p">]</span> <span class="o">-</span> <span class="n">left_top_cal</span></div><div class='line' id='LC78'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">left_bottom</span> <span class="o">=</span> <span class="n">wiimote</span><span class="o">.</span><span class="n">state</span><span class="p">[</span><span class="s">&#39;balance&#39;</span><span class="p">][</span><span class="s">&#39;left_bottom&#39;</span><span class="p">]</span> <span class="o">-</span> <span class="n">left_bottom_cal</span></div><div class='line' id='LC79'><br/></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">LEFT_RIGHT_MULTIPLIER</span> <span class="o">=</span> <span class="mf">1.2</span></div><div class='line' id='LC81'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">FRONT_BACK_MULTIPLIER</span> <span class="o">=</span> <span class="mf">1.2</span></div><div class='line' id='LC82'><br/></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lean</span> <span class="o">=</span> <span class="s">&quot;Indeterminate&quot;</span></div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># No one on the Balance Board yet		</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">((</span><span class="n">right_bottom</span> <span class="o">&lt;</span> <span class="mi">100</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">right_top</span> <span class="o">&lt;</span> <span class="mi">100</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">left_bottom</span> <span class="o">&lt;</span> <span class="mi">100</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">left_top</span> <span class="o">&lt;</span> <span class="mi">100</span><span class="p">)):</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lean</span> <span class="o">=</span> <span class="s">&quot;Stop&quot;</span></div><div class='line' id='LC88'><br/></div><div class='line' id='LC89'>		    <span class="c"># Leaning towards the front left of the Balance Board	</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="p">(((</span><span class="n">right_top</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">left_top</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">right_top</span><span class="p">))</span> <span class="o">&gt;=</span> <span class="n">LEFT_RIGHT_MULTIPLIER</span><span class="p">))</span> <span class="ow">and</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">((</span><span class="n">left_bottom</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">left_top</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">left_bottom</span><span class="p">))</span> <span class="o">&gt;=</span> <span class="n">FRONT_BACK_MULTIPLIER</span><span class="p">))):</span></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lean</span> <span class="o">=</span> <span class="s">&quot;Left Top&quot;</span></div><div class='line' id='LC93'><br/></div><div class='line' id='LC94'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Leaning towards the front right of the Balance Board	</span></div><div class='line' id='LC95'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="p">(((</span><span class="n">left_top</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span>  <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">right_top</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">left_top</span><span class="p">))</span> <span class="o">&gt;=</span> <span class="n">LEFT_RIGHT_MULTIPLIER</span><span class="p">))</span> <span class="ow">and</span></div><div class='line' id='LC96'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">((</span><span class="n">right_bottom</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">right_top</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">right_bottom</span><span class="p">))</span> <span class="o">&gt;=</span> <span class="n">FRONT_BACK_MULTIPLIER</span><span class="p">))):</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lean</span> <span class="o">=</span> <span class="s">&quot;Right Top&quot;</span></div><div class='line' id='LC98'><br/></div><div class='line' id='LC99'>		    <span class="c"># Leaning towards the back left of the Balance Board	</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="p">(((</span><span class="n">right_bottom</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">left_bottom</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">right_bottom</span><span class="p">))</span> <span class="o">&gt;=</span> <span class="n">LEFT_RIGHT_MULTIPLIER</span><span class="p">))</span> <span class="ow">and</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">((</span><span class="n">left_top</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">left_bottom</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">left_top</span><span class="p">))</span> <span class="o">&gt;=</span> <span class="n">FRONT_BACK_MULTIPLIER</span><span class="p">))):</span></div><div class='line' id='LC102'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lean</span> <span class="o">=</span> <span class="s">&quot;Left Bottom&quot;</span></div><div class='line' id='LC103'><br/></div><div class='line' id='LC104'>		    <span class="c"># Leaning towards the back right of the Balance Board	</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="p">(((</span><span class="n">right_top</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">right_bottom</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">right_top</span><span class="p">))</span> <span class="o">&gt;=</span> <span class="n">FRONT_BACK_MULTIPLIER</span><span class="p">))</span> <span class="ow">and</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">((</span><span class="n">left_bottom</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">right_bottom</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">left_bottom</span><span class="p">))</span> <span class="o">&gt;=</span> <span class="n">LEFT_RIGHT_MULTIPLIER</span><span class="p">))):</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lean</span> <span class="o">=</span> <span class="s">&quot;Right Bottom&quot;</span></div><div class='line' id='LC108'><br/></div><div class='line' id='LC109'>		    <span class="c"># Leaning towards the front middle of the Balance Board	</span></div><div class='line' id='LC110'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="p">(((</span><span class="n">right_bottom</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">right_top</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">right_bottom</span><span class="p">))</span> <span class="o">&gt;=</span> <span class="n">FRONT_BACK_MULTIPLIER</span><span class="p">))</span> <span class="ow">and</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">((</span><span class="n">left_bottom</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">left_top</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">left_bottom</span><span class="p">))</span> <span class="o">&gt;=</span> <span class="n">FRONT_BACK_MULTIPLIER</span><span class="p">))</span> <span class="ow">and</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">((</span><span class="n">right_top</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">left_top</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">right_top</span><span class="p">))</span> <span class="o">&lt;</span> <span class="n">LEFT_RIGHT_MULTIPLIER</span><span class="p">))):</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lean</span> <span class="o">=</span> <span class="s">&quot;Middle Top&quot;</span></div><div class='line' id='LC114'><br/></div><div class='line' id='LC115'>		    <span class="c"># Leaning towards the back middle of the Balance Board	</span></div><div class='line' id='LC116'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="p">(((</span><span class="n">right_top</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">right_bottom</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">right_top</span><span class="p">))</span> <span class="o">&gt;=</span> <span class="n">FRONT_BACK_MULTIPLIER</span><span class="p">))</span> <span class="ow">and</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">((</span><span class="n">left_top</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">left_bottom</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">left_top</span><span class="p">))</span> <span class="o">&gt;=</span> <span class="n">FRONT_BACK_MULTIPLIER</span><span class="p">))</span> <span class="ow">and</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">((</span><span class="n">right_bottom</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">left_bottom</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">right_bottom</span><span class="p">))</span> <span class="o">&lt;</span> <span class="n">LEFT_RIGHT_MULTIPLIER</span><span class="p">))):</span></div><div class='line' id='LC119'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lean</span> <span class="o">=</span> <span class="s">&quot;Middle Bottom&quot;</span></div><div class='line' id='LC120'><br/></div><div class='line' id='LC121'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># Anywhere in the middle of the board considered to be Stop			</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="p">(((</span><span class="n">right_bottom</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">right_top</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">right_bottom</span><span class="p">))</span> <span class="o">&lt;</span> <span class="n">FRONT_BACK_MULTIPLIER</span><span class="p">))</span> <span class="ow">and</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">((</span><span class="n">left_bottom</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">or</span> <span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">left_top</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">left_bottom</span><span class="p">))</span> <span class="o">&lt;</span> <span class="n">FRONT_BACK_MULTIPLIER</span><span class="p">))):</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">lean</span> <span class="o">=</span> <span class="s">&quot;Stop&quot;</span></div><div class='line' id='LC125'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="n">lean</span></div><div class='line' id='LC126'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC127'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#print (&#39;Balance Report: right_top=%s right_bottom=%s &#39; + \</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#       &#39;left_top=%s left_bottom=%s&#39;) % \</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#      (right_top, right_bottom, left_top, left_bottom)</span></div><div class='line' id='LC130'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">((</span><span class="n">right_bottom</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">right_top</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">left_bottom</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">left_top</span> <span class="o">!=</span> <span class="mi">0</span><span class="p">)):</span></div><div class='line' id='LC131'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="p">(</span><span class="s">&#39;RT/RB = </span><span class="si">%.2f</span><span class="s"> LT/LB = </span><span class="si">%.2f</span><span class="s"> RT/LT = </span><span class="si">%.2f</span><span class="s"> RB/LB = </span><span class="si">%.2f</span><span class="s">&#39;</span><span class="p">)</span> <span class="o">%</span> \</div><div class='line' id='LC132'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="nb">abs</span><span class="p">(</span><span class="n">right_top</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">right_bottom</span><span class="p">)),</span> <span class="nb">abs</span><span class="p">(</span><span class="n">left_top</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">left_bottom</span><span class="p">)),</span> <span class="nb">abs</span><span class="p">(</span><span class="n">right_top</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">left_top</span><span class="p">)),</span> <span class="nb">abs</span><span class="p">(</span><span class="n">right_bottom</span><span class="o">/</span><span class="nb">float</span><span class="p">(</span><span class="n">left_bottom</span><span class="p">)))</span> 	  </div><div class='line' id='LC133'><br/></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">lean</span> <span class="o">==</span> <span class="s">&quot;Left Top&quot;</span><span class="p">):</span></div><div class='line' id='LC135'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    # 0x5X for left forward. 0x51 very slow. 0x5F fastest</span></div><div class='line' id='LC136'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sock</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x5A</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC137'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">lean</span> <span class="o">==</span> <span class="s">&quot;Right Top&quot;</span><span class="p">):</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    # 0x6X for right forward. 0x11 very slow. 0x1F fastest</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sock</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x6A</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC140'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">lean</span> <span class="o">==</span> <span class="s">&quot;Middle Top&quot;</span><span class="p">):</span></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    # 0x1X for straight forward. 0x11 very slow. 0x1F fastest</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sock</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x1A</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">lean</span> <span class="o">==</span> <span class="s">&quot;Left Bottom&quot;</span><span class="p">):</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    # 0x7X for left backwards. 0x71 very slow. 0x7F fastest</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sock</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x7A</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">lean</span> <span class="o">==</span> <span class="s">&quot;Right Bottom&quot;</span><span class="p">):</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    # 0x8X for right backwards. 0x81 very slow. 0x8F fastest</span></div><div class='line' id='LC148'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sock</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x8A</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC149'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">lean</span> <span class="o">==</span> <span class="s">&quot;Middle Bottom&quot;</span><span class="p">):</span></div><div class='line' id='LC150'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    # 0x2X for straight backward. 0x21 very slow. 0x2F fastest</span></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sock</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x2A</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC152'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="p">(</span><span class="n">lean</span> <span class="o">==</span> <span class="s">&quot;Stop&quot;</span><span class="p">):</span></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#    #stop</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sock</span><span class="o">.</span><span class="n">send</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\x00</span><span class="s">&#39;</span><span class="p">)</span></div><div class='line' id='LC155'><br/></div><div class='line' id='LC156'><span class="n">main</span><span class="p">()</span></div></pre></div></td>
         </tr>
       </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.03070s from github-fe121-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-c23f6bb20db24ab07b4ee77598ac060d1ca974e3.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-878d4b5b0998b0ef887f50f5b3e0e3d3eb733106.js" type="text/javascript"></script>
      
      
        <script async src="https://www.google-analytics.com/analytics.js"></script>
  </body>
</html>

